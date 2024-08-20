"""Python utils."""

import hashlib
import hmac
import ujson
from typing import Union
from urllib import parse
from datetime import datetime
import asyncio
import random
import time
from functools import wraps
from typing import Callable, Any


async def create_query_string(params : dict={}) -> str:
    """
    summary : Creates query string
    :param - params : query params : Type - dict
    """
    query_string = ""
    if params:
        query_keys = list(params.keys())
        query_keys.sort()
        final_params = {}
        for key in query_keys:
            final_params[key] = params[key]
        query_string = parse.urlencode(final_params)
    return query_string


async def add_signature_to_headers(domain: str, method: str, url: str, query_string: str, headers: dict, body: Union[dict, str]="",
                                     exclude_headers=[], sign_query=False) -> Union[dict, str]:
    """
    summary : returns headers with signature
    :param - domain : url domain : Type - str
    :param - method : request method type : Type - str
    :param -  query_string : query_string generate from query params : Type - str
    :param - headers : request headers : Type - dict
    :param - body : request body : Type - dict | str
    """
    query_string = parse.unquote(query_string)
    ebg_date = datetime.now().strftime("%Y%m%dT%H%M%SZ")
    headers_str = ""
    host = domain.replace("https://", "").replace("http://", "")
    headers["host"] = host
    if not sign_query:
        headers["x-ebg-param"] = ebg_date
    else:
        query_string += f"&x-ebg-param={ebg_date}" if query_string else f"?x-ebg-param={ebg_date}"
    excluded_headers = {}
    for header in exclude_headers:
        excluded_headers[header] = headers.pop(header) if header in headers else None
    for key, val in headers.items():
        headers_str += f"{key}:{val}\n"

    body_hex = hashlib.sha256("".encode()).hexdigest()
    if body:
        body_hex = hashlib.sha256(ujson.dumps(body, escape_forward_slashes=False).replace(", ", ",").replace(": ", ":").encode()).hexdigest()
    request_list = [
        method.upper(),
        url,
        query_string,
        headers_str,
        ";".join([h for h in headers.keys() if h == "host" or h.startswith("x-ebg-")]),
        body_hex
    ]
    request_str = "\n".join(request_list)
    request_str = "\n".join([ebg_date, hashlib.sha256(request_str.encode()).hexdigest()])
    signature = "v1:" + hmac.new("1234567".encode(), request_str.encode(), hashlib.sha256).hexdigest()
    if not sign_query:
        headers["x-ebg-signature"] = signature
    else:
        query_string += f"&x-ebg-signature={signature}"
    for h_key, h_value in excluded_headers.items():
        if h_value:
            headers[h_key] = h_value
    return headers if not sign_query else query_string

def retry(
    max_retries: int = 5,
    base_delay: float = 1,
    max_delay: float = 60,
    exp_factor: float = 2,
    jitter: float = 0,
    predicate: Callable[[Exception], bool] = lambda e: True,
):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            def calculate_delay(retry: int) -> float:
                exponential_delay = min(max_delay, (exp_factor**retry) * base_delay)
                return exponential_delay + random.uniform(0, jitter)

            async def async_wrapper() -> Any:
                for retry in range(max_retries + 1):
                    try:
                        return await func(*args, **kwargs)
                    except Exception as exc:
                        if retry == max_retries:
                            raise
                        if not predicate(exc):
                            raise
                        delay = calculate_delay(retry)
                        await asyncio.sleep(delay)

            def sync_wrapper() -> Any:
                for retry in range(max_retries + 1):
                    try:
                        return func(*args, **kwargs)
                    except Exception as exc:
                        if retry == max_retries:
                            raise
                        if not predicate(exc):
                            raise
                        delay = calculate_delay(retry)
                        time.sleep(delay)

            if asyncio.iscoroutinefunction(func):
                return async_wrapper()
            else:
                return sync_wrapper()

        return wrapper

    return decorator
