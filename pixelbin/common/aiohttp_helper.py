"""Python code/pixelbin/common/aiohttp_helper.py."""

import time

import aiohttp
import ujson
from typing import Union

from .constants import HTTP_TIMEOUT
from .date_helper import get_ist_now


class AiohttpHelper:
    """Aiohttp Helper."""

    @staticmethod
    def __get_formdata():
        return aiohttp.formdata.FormData(quote_fields=False)

    @staticmethod
    async def parse_data(data):
        """parse_data."""
        try:
            text = ujson.loads(data)

        except ValueError:
            text = {}

        return text

    async def __make_request(
        self,
        method: str,
        url: str,
        params: dict,
        data: Union[str, aiohttp.formdata.FormData],
        headers: dict,
        timeout_allowed: int,
        trust_env: bool,
    ) -> dict:
        start_time = time.time()
        timeout = aiohttp.ClientTimeout(total=timeout_allowed)
        response = {
            "url": url,
            "method": method,
            "params": params,
            "data": data,
            "external_call_request_time": str(get_ist_now()),
            "status_code": None,
            "text": "",
            "headers": "",
            "cookies": None,
            "error_message": "",
        }

        async with aiohttp.ClientSession(
            headers=headers, timeout=timeout, trust_env=trust_env
        ) as session:
            async with session.request(
                method.upper(), url=url, params=params, data=data
            ) as resp:
                response["status_code"] = resp.status
                response["headers"] = dict(resp.headers)
                response["cookies"] = dict(resp.cookies)
                try:
                    response["content"] = (
                        await resp.content.read()
                    )  # resp.content is a StreamReader
                    response["text"] = response["content"].decode()  # converting to str
                except UnicodeDecodeError as err:
                    response["error_message"] = (
                        f"Error occurred while converting bytes to string - {err}"
                    )
                    response["latency"] = time.time() - start_time
                    response["json"] = await self.parse_data(response["text"])
                except Exception as request_error:
                    response["status_code"] = 999
                    response["latency"] = time.time() - start_time
                    response["text"] = request_error
        return response

    async def request(
        self,
        method: str,
        url: str,
        params: dict,
        data: dict,
        headers: dict,
        timeout_allowed: int = HTTP_TIMEOUT,
        trust_env: bool = False,
    ) -> dict:
        """
        summary - call api using aiohttp

        :param - method : request method type : Type - str
        :param - url : url to be hit : Type - str
        :param - params : query params : Type - dict
        :param - data : request body data : Type - dict
        :param - headers : request headers : Type - dict
        :param - timeout_allowed : timeout for request in seconds : Type - int
        """
        if data:
            if "file" in data.keys():
                form_data = self.__get_formdata()
                for k, v in data.items():
                    if isinstance(v, list):
                        for ele in v:
                            form_data.add_field(k, ele)
                    else:
                        value = (
                            ujson.dumps(v, escape_forward_slashes=False)
                            if isinstance(v, dict) or isinstance(v, bool)
                            else v
                        )
                        form_data.add_field(k, value)
                data = form_data
            else:
                data = ujson.dumps(data, escape_forward_slashes=False)

        response = await self.__make_request(
            method=method,
            url=url,
            params=params,
            data=data,
            headers=headers,
            timeout_allowed=timeout_allowed,
            trust_env=trust_env,
        )
        return response
