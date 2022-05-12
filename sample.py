import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_TOKEN",
})

pixelbin = PixelbinClient(config)


# Sync method call
try:
    result = pixelbin.assets.fileUpload(file=open("../../../1.jpeg","rb"))
    # use result
    print(result)
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.get_event_loop().run_until_complete(pixelbin.assets.fileUpload(file=open("../../../1.jpeg","rb")))
    # use result
    print(result)
except Exception as e:
    print(e)