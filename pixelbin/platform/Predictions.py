import asyncio
import ujson
import io
from typing import Any, Dict, List, Optional

from .PlatformAPIClient import APIClient
from .PixelbinConfig import PixelbinConfig
from ..common.exceptions import (
    PixelbinIllegalArgumentError,
    PixelbinServerResponseError,
)


class Predictions:
    def __init__(self, config: PixelbinConfig):
        self.config = config

    async def createAsync(
        self,
        name: str,
        input: Dict[str, Any] = None,
        webhook: Optional[str] = None,
    ) -> Dict[str, Any]:
        if not isinstance(name, str) or not name:
            raise PixelbinIllegalArgumentError("name (string) is required")

        parts = name.split("_")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            raise PixelbinIllegalArgumentError(
                "name must be in 'plugin_operation' format, e.g. 'erase_bg'"
            )
        plugin, operation = parts[0], parts[1]

        input = input or {}

        body: Dict[str, Any] = {}
        if webhook:
            body["webhook"] = webhook

        def is_url(value: str) -> bool:
            return isinstance(value, str) and value.lower().startswith(
                ("http://", "https://")
            )

        def wrap_file_like(val: Any, key: str) -> Any:
            """Normalize bytes/streams or {value, filename} dict into file-like with .name for filename.
            aiohttp infers filename from object's .name attribute when not explicitly provided.
            """
            # Support wrapper dict: { value: <bytes|file>, filename?: str }
            if isinstance(val, dict) and "value" in val:
                payload = val.get("value")
                filename = val.get("filename")
            else:
                payload = val
                filename = None

            # Bytes/bytearray -> BytesIO with name
            if isinstance(payload, (bytes, bytearray)):
                bio = io.BytesIO(payload)
                try:
                    setattr(bio, "name", filename or f"{key}.jpg")
                except Exception:
                    pass
                return bio

            # File-like object -> ensure it has a name
            if hasattr(payload, "read"):
                try:
                    has_name = hasattr(payload, "name") and isinstance(
                        getattr(payload, "name"), str
                    )
                except Exception:
                    has_name = False
                if not has_name:
                    try:
                        setattr(payload, "name", filename or f"{key}.jpg")
                    except Exception:
                        pass
                return payload

            # Other types unchanged
            return val

        def is_file_like(val: Any) -> bool:
            if isinstance(val, (bytes, bytearray)):
                return True
            if hasattr(val, "read"):
                return True
            if isinstance(val, dict) and "value" in val:
                inner = val.get("value")
                return isinstance(inner, (bytes, bytearray)) or hasattr(inner, "read")
            if isinstance(val, list):
                return any(is_file_like(v) for v in val)
            return False

        has_binary = any(is_file_like(v) for v in (input or {}).values())

        for key, value in input.items():
            if value is None:
                continue
            field_name = f"input.{key}"
            if isinstance(value, list):
                processed_list: List[Any] = []
                for v in value:
                    # For each element, wrap bytes/streams; JSON-encode plain dicts
                    if isinstance(v, dict) and "value" not in v:
                        processed_list.append(
                            ujson.dumps(v, escape_forward_slashes=False)
                        )
                    else:
                        processed_list.append(wrap_file_like(v, key))
                body[field_name] = processed_list
            elif isinstance(value, dict) and "value" not in value:
                # Plain objects (non-file wrapper) -> JSON string
                body[field_name] = ujson.dumps(value, escape_forward_slashes=False)
            else:
                # Bytes/streams and wrapper dicts -> ensure filename; primitives/urls sent as-is
                body[field_name] = wrap_file_like(value, key)

        content_type = "multipart/form-data" if has_binary else "application/json"

        response = await APIClient.execute(
            conf=self.config,
            method="post",
            url=f"/service/platform/transformation/v1.0/predictions/{plugin}/{operation}",
            query={},
            body=body,
            contentType=content_type,
        )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(
                str(response["content"]), response["status_code"]
            )
        return ujson.loads(response["content"])

    def create(
        self,
        name: str,
        input: Dict[str, Any] = None,
        webhook: Optional[str] = None,
    ) -> Dict[str, Any]:
        return asyncio.get_event_loop().run_until_complete(
            self.createAsync(name=name, input=input or {}, webhook=webhook)
        )

    async def getAsync(self, request_id: str) -> Dict[str, Any]:
        if not isinstance(request_id, str) or not request_id:
            raise PixelbinIllegalArgumentError("requestId (string) is required")
        path = f"/service/platform/transformation/v1.0/predictions/{request_id}"
        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=path,
            query={},
            body=None,
            contentType="",
        )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(
                str(response["content"]), response["status_code"]
            )
        return ujson.loads(response["content"])

    def get(self, request_id: str) -> Dict[str, Any]:
        return asyncio.get_event_loop().run_until_complete(self.getAsync(request_id))

    async def waitAsync(
        self, request_id: str, options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        if not request_id:
            raise PixelbinIllegalArgumentError("requestId is required")
        DEFAULT_MIN_TIMEOUT = 4.0  # seconds
        DEFAULT_RETRIES = 150
        DEFAULT_FACTOR = 1.0
        opts = options or {}
        # Parse and clamp options
        raw_interval = (
            float(opts.get("retryInterval"))
            if isinstance(opts.get("retryInterval"), (int, float))
            else DEFAULT_MIN_TIMEOUT
        )
        raw_attempts = (
            int(opts.get("maxAttempts"))
            if isinstance(opts.get("maxAttempts"), int)
            else DEFAULT_RETRIES
        )
        raw_factor = (
            float(opts.get("retryFactor"))
            if isinstance(opts.get("retryFactor"), (int, float))
            else DEFAULT_FACTOR
        )

        attempts = max(1, min(150, int(raw_attempts)))
        factor = max(1.0, min(3.0, raw_factor))
        interval = max(1.0, min(60.0, float(raw_interval)))

        last_status: Dict[str, Any] = {}
        for _ in range(attempts):
            s = await self.getAsync(request_id)
            last_status = s
            if s and s.get("status") in ("SUCCESS", "FAILURE"):
                return s
            await asyncio.sleep(interval)
            try:
                interval = interval * factor
            except Exception:
                pass
        return last_status

    def wait(
        self, request_id: str, options: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        return asyncio.get_event_loop().run_until_complete(
            self.waitAsync(request_id, options)
        )

    async def create_and_waitAsync(
        self,
        name: str,
        input: Dict[str, Any] = None,
        webhook: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        job = await self.createAsync(name=name, input=input or {}, webhook=webhook)
        return await self.waitAsync(job["_id"], options)

    def create_and_wait(
        self,
        name: str,
        input: Dict[str, Any] = None,
        webhook: Optional[str] = None,
        options: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return asyncio.get_event_loop().run_until_complete(
            self.create_and_waitAsync(
                name=name, input=input or {}, webhook=webhook, options=options
            )
        )

    async def listAsync(self) -> List[Dict[str, Any]]:
        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=f"/service/public/transformation/v1.0/predictions",
            query={},
            body={},
            contentType="",
        )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(
                str(response["content"]), response["status_code"]
            )
        return ujson.loads(response["content"])

    def list(self) -> List[Dict[str, Any]]:
        return asyncio.get_event_loop().run_until_complete(self.listAsync())

    async def get_schemaAsync(self, name: str) -> Dict[str, Any]:
        if not isinstance(name, str) or not name:
            raise PixelbinIllegalArgumentError("name (string) is required")
        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=f"/service/public/transformation/v1.0/predictions/schema/{name}",
            query={},
            body={},
            contentType="",
        )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(
                str(response["content"]), response["status_code"]
            )
        return ujson.loads(response["content"])

    def get_schema(self, name: str) -> Dict[str, Any]:
        return asyncio.get_event_loop().run_until_complete(self.get_schemaAsync(name))
