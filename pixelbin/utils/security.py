import time
import hmac
import hashlib
from urllib import parse
from ..common.exceptions import (
    PixelbinIllegalArgumentError,
)


def hmac_sha256(key: str, message: str):
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()


def generate_signature(url_path: str, expiry_timestamp: int, key: str):
    if url_path.startswith("/"):
        url_path = url_path[1:]
    signature = hmac_sha256(key, f"{url_path}{expiry_timestamp}")
    return signature


def sign_url(url: str, expiry_seconds: int, access_key: str, token: str):
    if not isinstance(expiry_seconds, int):
        raise PixelbinIllegalArgumentError("expiry_seconds must be an integer")

    if not isinstance(access_key, (int, str)):
        raise PixelbinIllegalArgumentError("access_key must be a string")

    if not isinstance(token, str):
        raise PixelbinIllegalArgumentError("token must be a string")

    url_parts = parse.urlparse(url)
    url_path = url_parts.path
    url_query = parse.parse_qs(url_parts.query)

    if url_query.get("pbs"):
        raise PixelbinIllegalArgumentError("URL already has a signature")

    expiry_timestamp = int(time.time()) + expiry_seconds

    signature = generate_signature(url_path, expiry_timestamp, token)

    url_query["pbs"] = signature
    url_query["pbe"] = expiry_timestamp
    url_query["pbt"] = access_key

    url_parts = url_parts._replace(query=parse.urlencode(url_query, doseq=True))

    return parse.urlunparse(url_parts)
