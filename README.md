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

## Security Utils

### For generating Signed URLs

Generate a signed PixelBin url

| Parameter              | Description                                          | Example                                                                                    |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `url` (string)         | A valid Pixelbin URL to be signed                    | `https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg` |
| `expiry_seconds` (int) | Number of seconds the signed URL should be valid for | `20`                                                                                       |
| `access_key` (string)  | Access key of the token used for signing             | `6227274d-92c9-4b74-bef8-2528542516d8`                                                     |
| `token` (string)       | Value of the token used for signing                  | `dummy-token`                                                                              |

Example:

```python
from pixelbin.utils.security import sign_url

signed_url = sign_url(
    "https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg", # url
    20, # expiry_seconds
    "6227274d-92c9-4b74-bef8-2528542516d8", # access_key
    "dummy-token", # token
);
# signed_url
# https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg?pbs=8eb6a00af74e57967a42316e4de238aa88d92961649764fad1832c1bff101f25&pbe=1695635915&pbt=6227274d-92c9-4b74-bef8-2528542516d8
```

Usage with custom domain url

```python
from pixelbin.utils.security import sign_url

signed_url = sign_url(
    "https://test.example.com/v2/original/__playground/playground-default.jpeg", # url
    30, # expirySeconds
    22, # tokenId
    "dummy-token", # token
);
# signedUrl
# https://test.example.com/v2/original/__playground/playground-default.jpeg?pbs=1aef31c1e0ecd8a875b1d3184f324327f4ab4bce419d81d1eb1a818ee5f2e3eb&pbe=1695705975&pbt=22
```

## URL Utils

Pixelbin provides url utilities to construct and deconstruct Pixelbin urls.

### url_to_obj

Deconstruct a pixelbin url

| parameter               | description                                                        | example                                                                                               |
| ----------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| `url` (string)          | A valid Pixelbin URL                                               | `https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg` |
| `opts` (Object)         | Options for the conversion                                         | Default: `{ isCustomDomain: False }`                                                                  |
| `opts.is_custom_domain` | Indicates if the URL belongs to a custom domain (default: `False`) |

**Returns**:

| Property                  | Description                                          | Example                               |
| ------------------------- | ---------------------------------------------------- | ------------------------------------- |
| `baseURL` (string)        | Base path of the URL                                 | `https://cdn.pixelbin.io`             |
| `filePath` (string)       | Path to the file on Pixelbin storage                 | `/path/to/image.jpeg`                 |
| `version` (string)        | Version of the URL                                   | `v2`                                  |
| `cloudName` (string)      | Cloud name from the URL                              | `your-cloud-name`                     |
| `transformations` (array) | A list of transformation objects                     | `[{ "plugin": "t", "name": "flip" }]` |
| `zone` (string)           | Zone slug from the URL                               | `z-slug`                              |
| `pattern` (string)        | Transformation pattern extracted from the URL        | `t.resize(h:100,w:200)~t.flip()`      |
| `worker` (boolean)        | Indicates if the URL is a URL Translation Worker URL | `False`                               |
| `workerPath` (string)     | Input path to a URL Translation Worker               | `resize:w200,h400/folder/image.jpeg`  |
| `options` (Object)        | Query parameters added, such as "dpr" and "f_auto"   | `{ dpr: 2.5, f_auto: True}`           |

Example:

```python
from pixelbin.utils.url import url_to_obj

pixelbinUrl = "https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg?dpr=2.0&f_auto=true"
obj = url_to_obj(pixelbinUrl)
# obj
# {
#     "cloudName": "your-cloud-name",
#     "zone": "z-slug",
#     "version": "v2",
#     "options": {
#         "dpr": 2.0,
#         "f_auto": True,
#     },
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

```python
from pixelbin.utils.url import url_to_obj

customDomainUrl =
    "https://xyz.designify.media/v2/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg";
obj = url_to_obj(customDomainUrl, opts={ is_custom_domain: True })
# obj
# {
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
#     "baseUrl": "https://xyz.designify.media",
#     "wrkr": False,
#     "workerPath": "",
#     "options": {}
# }
```

```python
workerUrl =
    "https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/wrkr/resize:h100,w:200/folder/image.jpeg";

obj = url_to_obj(workerUrl)
# obj
# {
#     "cloudName": "your-cloud-name",
#     "zone": "z-slug",
#     "version": "v2",
#     "transformations": [],
#     "filePath": "",
#     "worker": True,
#     "workerPath": "resize:h100,w:200/folder/image.jpeg",
#     "baseUrl": "https://cdn.pixelbin.io"
#     "options": {}
# }
```

### obj_to_url

Converts the extracted url obj to a Pixelbin url.

| Property                   | Description                                          | Example                               |
| -------------------------- | ---------------------------------------------------- | ------------------------------------- |
| `cloudName` (string)       | The cloudname extracted from the URL                 | `your-cloud-name`                     |
| `zone` (string)            | 6 character zone slug                                | `z-slug`                              |
| `version` (string)         | CDN API version                                      | `v2`                                  |
| `transformations` (array)  | Extracted transformations from the URL               | `[{ "plugin": "t", "name": "flip" }]` |
| `filePath` (string)        | Path to the file on Pixelbin storage                 | `/path/to/image.jpeg`                 |
| `baseUrl` (string)         | Base URL                                             | `https://cdn.pixelbin.io/`            |
| `isCustomDomain` (boolean) | Indicates if the URL is for a custom domain          | `False`                               |
| `worker` (boolean)         | Indicates if the URL is a URL Translation Worker URL | `False`                               |
| `workerPath` (string)      | Input path to a URL Translation Worker               | `resize:w200,h400/folder/image.jpeg`  |
| `options` (Object)         | Query parameters added, such as "dpr" and "f_auto"   | `{ "dpr": 2.0, "f_auto": True }`      |

```python
from pixelbin.utils.url import obj_to_url

obj = {
    cloudName: "your-cloud-name",
    zone: "z-slug",
    version: "v2",
    options: {
        dpr: 2.0,
        f_auto: True,
    },
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
# https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg?dpr=2.0&f_auto=true
```

Usage with custom domain

```python
from pixelbin.utils.url import obj_to_url

obj = {
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
    baseUrl: "https://xyz.designify.media",
    isCustomDomain: True,
};
url = Pixelbin.utils.objToUrl(obj); # obj is as shown above
# url
# https://xyz.designify.media/v2/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg
```

Usage with URL Translation Worker

```python
from pixelbin.utils.url import obj_to_url

obj = {
    cloudName: "your-cloud-name",
    zone: "z-slug",
    version: "v2",
    transformations: [],
    filePath: "",
    worker: True,
    workerPath: "resize:h100,w:200/folder/image.jpeg",
    baseUrl: "https://cdn.pixelbin.io",
};
url = Pixelbin.utils.objToUrl(obj); # obj is as shown above
# url
# https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/wrkr/resize:h100,w:200/folder/image.jpeg
```

## Documentation

-   [API docs](documentation/platform/README.md)
