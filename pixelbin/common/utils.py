"""Python utils."""

import hashlib
import hmac
import json
import ujson
from typing import Dict, Text
from urllib import parse
from datetime import datetime
from .exceptions import RequiredParametersError


async def validate_required_query_params(proccessed_params: Dict, params: Dict):
    """Checks if required params are present or not."""
    for r_param in proccessed_params["required"]:
        r_param_name = r_param["name"]
        if ((r_param_name not in params) or not params[r_param_name]) and r_param_name != "company_id" and r_param_name != "application_id":
            raise RequiredParametersError(message="{} missing".format(r_param["name"]))


async def create_url_with_params(domain: Text = "", api_url: Text = "", proccessed_params: Text = "", **kwargs):
    """Creates url with params"""
    params = {}
    final_url = domain + api_url
    for key, value in kwargs.items():
        if value:
            new_key = key.replace("__", "-")
            params[new_key] = value
            if new_key in final_url:
                final_url.replace(new_key, key)
    await validate_required_query_params(json.loads(proccessed_params), params)
    final_url = final_url.format(**params)
    query_string = parse.urlencode(params)
    if query_string:
        final_url += "?" + query_string
    return final_url


async def create_url_with_params_and_query_string(domain: Text = "", api_url: Text = "", params={}):
    """Creates url with params"""
    final_url = domain + api_url
    query_string = ""
    if params:
        query_keys = list(params.keys())
        query_keys.sort()
        final_params = {}
        for key in query_keys:
            final_params[key] = params[key]
        final_url = final_url.format(**final_params)
        query_string = parse.urlencode(final_params)
        if query_string:
            final_url += "?" + query_string
    return final_url, query_string


async def create_url_without_domain(url: Text, **kwargs):
    """Returns url without domain replacing variables."""
    params = {}
    for key, value in kwargs.items():
        if value:
            new_key = key.replace("__", "-")
            params[new_key] = value
            if new_key in url:
                url.replace(new_key, key)
    final_url = url.format(**params)
    return final_url


async def create_query_string(**kwargs):
    """Return query string."""
    params = {}
    for key, value in kwargs.items():
        if value:
            new_key = key.replace("__", "-")
            params[new_key] = value
    query_keys = list(params.keys())
    query_keys.sort()
    final_params = {}
    for key in query_keys:
        final_params[key] = params[key]
    query_string = parse.urlencode(final_params)
    return query_string


async def get_headers_with_signature(domain: Text, method: Text, url: Text, query_string: Text, headers: Dict, body="",
                                     exclude_headers=[], sign_query=False):
    """Returns headers with signature."""
    query_string = parse.unquote(query_string)
    fp_date = datetime.now().strftime("%Y%m%dT%H%M%SZ")
    headers_str = ""
    host = domain.replace("https://", "").replace("http://", "")
    headers["host"] = host
    if not sign_query:
        headers["x-fp-date"] = fp_date
    else:
        query_string += f"&x-fp-date={fp_date}" if query_string else f"?x-fp-date={fp_date}"
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
        ";".join([h for h in headers.keys() if h == "host" or h.startswith("x-fp-")]),
        body_hex
    ]
    request_str = "\n".join(request_list)
    request_str = "\n".join([fp_date, hashlib.sha256(request_str.encode()).hexdigest()])
    signature = "v1.1:" + hmac.new("1234567".encode(), request_str.encode(), hashlib.sha256).hexdigest()
    if not sign_query:
        headers["x-fp-signature"] = signature
    else:
        query_string += f"&x-fp-signature={signature}"
    for h_key, h_value in excluded_headers.items():
        if h_value:
            headers[h_key] = h_value
    return headers if not sign_query else query_string


async def add_signature_to_headers(domain: Text, method: Text, url: Text, query_string: Text, headers: Dict, body="",
                                     exclude_headers=[], sign_query=False):
    """Returns headers with signature."""
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