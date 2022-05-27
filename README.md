# Pixelbin Backend SDK for Python

Pixelbin Backend SDK for python helps you integrate the core Pixelbin features with your application.

## Getting Started

Getting started with Pixelbin Backend SDK for Python

### Installation

```
pip install pixelbin
```

---

### Usage

#### Quick Example

```python
import asyncio

from pixelbin import PixelbinClient, PixelbinConfig

# create client with your API_TOKEN
config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_TOKEN",
})

# Create a pixelbin instance
pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.listFiles()
    print(result)
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.get_event_loop().run_until_complete(pixelbin.assets.listFilesAsync())
    print(result)
except Exception as e:
    print(e)
```

## Utilities

Pixelbin provides url utilities to construct and deconstruct Pixelbin urls.

### url_to_obj

Deconstruct a pixelbin url

| parameter            | description          | example                                                                                               |
| -------------------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| pixelbinUrl (string) | A valid pixelbin url | `https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg` |

**Returns**:

| property                | description                            | example                    |
| ----------------------- | -------------------------------------- | -------------------------- |
| cloudName (string)      | The cloudname extracted from the url   | `your-cloud-name`          |
| zone (string)           | 6 character zone slug                  | `z-slug`                   |
| version (string)        | cdn api version                        | `v2`                       |
| transformations (array) | Extracted transformations from the url |                            |
| filePath                | Path to the file on Pixelbin storage   | `/path/to/image.jpeg`      |
| baseUrl (string)        | Base url                               | `https://cdn.pixelbin.io/` |

Example:

```python
from pixelbin.utils.url import url_to_obj

pixelbinUrl = "https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg"
obj = url_to_obj(pixelbinUrl)
# obj
# {
#     "cloudName": "your-cloud-name",
#     "zone": "z-slug",
#     "version": "v2",
#     "transformations": [
#         {
#             "plugin": "t",
#             "name": "resize",
#             "values": [
#                 {
#                     "key": "h",
#                     "value": "100"
#                 },
#                 {
#                     "key": "w",
#                     "value": "200"
#                 }
#             ]
#         },
#         {
#             "plugin": "t",
#             "name": "flip",
#         }
#     ],
#     "filePath": "path/to/image.jpeg",
#     "baseUrl": "https://cdn.pixelbin.io"
# }
```

### obj_to_url

Converts the extracted url obj to a Pixelbin url.

| property                | description                            | example                    |
| ----------------------- | -------------------------------------- | -------------------------- |
| cloudName (string)      | The cloudname extracted from the url   | `your-cloud-name`          |
| zone (string)           | 6 character zone slug                  | `z-slug`                   |
| version (string)        | cdn api version                        | `v2`                       |
| transformations (array) | Extracted transformations from the url |                            |
| filePath                | Path to the file on Pixelbin storage   | `/path/to/image.jpeg`      |
| baseUrl (string)        | Base url                               | `https://cdn.pixelbin.io/` |

```python
from pixelbin.utils.url import obj_to_url

obj = {
    cloudName: "your-cloud-name",
    zone: "z-slug",
    version: "v2",
    transformations: [
        {
            plugin: "t",
            name: "resize",
            values: [
                {
                    key: "h",
                    value: "100",
                },
                {
                    key: "w",
                    value: "200",
                },
            ],
        },
        {
            plugin: "t",
            name: "flip",
        },
    ],
    filePath: "path/to/image.jpeg",
    baseUrl: "https://cdn.pixelbin.io",
}
url = obj_to_url(obj) # obj is as shown above
# url
# https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg
```

## Documentation

-   [API docs](documentation/platform/README.md)
