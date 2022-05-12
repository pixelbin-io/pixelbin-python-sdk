"""Python code/pixelbin/common/aiohttp_helper.py."""

import time

import aiohttp
import ujson

from .constants import HTTP_TIMEOUT
from .date_helper import get_ist_now


class AiohttpHelper:
    """Aiohttp Helper."""

    @staticmethod
    async def parse_data(data):
        """parse_data."""
        try:
            text = ujson.loads(data)

        except ValueError:
            text = {}

        return text

    async def request(self, method, url, params, data, headers, timeout_allowed=HTTP_TIMEOUT):
        start_time = time.time()
        timeout = aiohttp.ClientTimeout(total=timeout_allowed)
        async with aiohttp.ClientSession(headers=headers, timeout=timeout) as session:
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
            if data:
                if "file" in data.keys():
                    fdata = aiohttp.formdata.FormData()
                    for k, v in data.items():
                        value = ujson.dumps(v, escape_forward_slashes=False) if isinstance(v, dict) or isinstance(v, bool) or isinstance(v, list) else v
                        fdata.add_field(k,value)
                    data = fdata
                else:
                    data = ujson.dumps(data, escape_forward_slashes=False)
            async with session.request(method.upper(), url=url, params=params, data=data) as resp:        
                response["status_code"] = resp.status
                response["headers"] = dict(resp.headers)
                response["cookies"] = dict(resp.cookies)
                try:
                    response["content"] = await resp.content.read()  # resp.content is a StreamReader
                    response["text"] = response["content"].decode()  # converting to str
                except UnicodeDecodeError as err:
                    response["error_message"] = f"Error occurred while converting bytes to string - {err}"
                    response["latency"] = time.time() - start_time
                    response["json"] = await self.parse_data(response["text"])
                except Exception as request_error:
                    response["status_code"] = 999
                    response["latency"] = (time.time() - start_time)
                    response["text"] = request_error
            return response
