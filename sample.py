import asyncio
from pixelbin import PixelbinClient, PixelbinConfig
from pixelbin.utils import security

config = PixelbinConfig(
    {
        "domain": "https://api.pixelbin.io",
        "apiSecret": "API_TOKEN",
    }
)

pixelbin = PixelbinClient(config)


# Sync method call
try:
    result = pixelbin.assets.fileUpload(file=open("./tests/1.jpeg", "rb"))
    # use result
    print(result)
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.get_event_loop().run_until_complete(
        pixelbin.assets.fileUpload(file=open("./tests/1.jpeg", "rb"))
    )
    # use result
    print(result)
except Exception as e:
    print(e)

# Generate signed urls
try:
    signed_url = security.sign_url(
        "https://test.example.com/v2/original/__playground/playground-default.jpeg",
        600,
        "c1adc3ba-75b6-492c-bfb4-e879f2ae61fe",
        "dummy-token",
    )
    print(signed_url)
except Exception as e:
    print(e)
