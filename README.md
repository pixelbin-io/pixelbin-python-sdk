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

## Uploader

### upload

Uploads a file to PixelBin with greater control over the upload process.

#### Arguments

| Argument            | Type                                                        | Required | Description                                                                                                                                                                                                                                           |
| ------------------- | ----------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file`              | `bytes` or `io.BufferedIOBase`                              | yes      | The file to be uploaded.                                                                                                                                                                                                                              |
| `name`              | `str`                                                       | no       | Name of the file.                                                                                                                                                                                                                                     |
| `path`              | `str`                                                       | no       | Path of the containing folder.                                                                                                                                                                                                                        |
| `format`            | `str`                                                       | no       | Format of the file.                                                                                                                                                                                                                                   |
| `access`            | [AccessEnum](./documentation/platform/ASSETS.md#accessenum) | no       | Access level of the asset, can be either `'public-read'` or `'private'`.                                                                                                                                                                              |
| `tags`              | `list[str]`                                                 | no       | Tags associated with the file.                                                                                                                                                                                                                        |
| `metadata`          | `dict`                                                      | no       | Metadata associated with the file.                                                                                                                                                                                                                    |
| `overwrite`         | `bool`                                                      | no       | Overwrite flag. If set to `True`, will overwrite any file that exists with the same path, name, and type. Defaults to `False`.                                                                                                                        |
| `filenameOverride`  | `bool`                                                      | no       | If set to `True`, will add unique characters to the name if an asset with the given name already exists. If the overwrite flag is set to `True`, preference will be given to the overwrite flag. If both are set to `False`, an error will be raised. |
| `expiry`            | `int`                                                       | no       | Expiry time in seconds for the underlying signed URL. Defaults to 3000 seconds.                                                                                                                                                                       |
| `uploadOptions`     | `dict`                                                      | no       | Additional options for fine-tuning the upload process. Default: `{ chunk_size: 10 * 1024 * 1024, max_retries: 2, concurrency: 3, exponential_factor: 2 }`.                                                                                            |
| `chunkSize`         | `int`                                                       | no       | Size of each chunk to upload. Default is 10 megabytes.                                                                                                                                                                                                |
| `maxRetries`        | `int`                                                       | no       | Maximum number of retries if an upload fails. Default is 2 retries.                                                                                                                                                                                   |
| `concurrency`       | `int`                                                       | no       | Number of concurrent chunk upload tasks. Default is 3 concurrent chunk uploads.                                                                                                                                                                       |
| `exponentialFactor` | `int`                                                       | no       | The exponential factor for retry delay. Default is 2.                                                                                                                                                                                                 |

#### Returns

`dict`: On success, returns a dictionary containing the details of the uploaded file.

| Property     | Description                                                  | Example                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `orgId`      | Organization ID                                              | `5320086`                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `type`       | Type of the uploaded entity                                  | `file`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `name`       | Name of the file                                             | `testfile.jpeg`                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `path`       | Path of the containing folder                                | `/path/to/image.jpeg`                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `fileId`     | ID of the file                                               | `testfile.jpeg`                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `access`     | Access level of the asset, can be `public-read` or `private` | `public-read`                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `tags`       | Tags associated with the file                                | `["tag1", "tag2"]`                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `metadata`   | Metadata associated with the file                            | `{"source":"", "publicUploadId":""}`                                                                                                                                                                                                                                                                                                                                                                                                       |
| `format`     | File format                                                  | `jpeg`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `assetType`  | Type of asset                                                | `image`                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `size`       | File size (in bytes)                                         | `37394`                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `width`      | File width (in pixels)                                       | `720`                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `height`     | File height (in pixels)                                      | `450`                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `context`    | File metadata and additional context                         | `{"steps":[],"req":{"headers":{},"query":{}},"meta":{"format":"png","size":195337,"width":812,"height":500,"space":"srgb","channels":4,"depth":"uchar","density":144,"isProgressive":false,"resolutionUnit":"inch","hasProfile":true,"hasAlpha":true,"extension":"jpeg","contentType":"image/png","assetType":"image","isImageAsset":true,"isAudioAsset":false,"isVideoAsset":false,"isRawAsset":false,"isTransformationSupported":true}}` |
| `isOriginal` | Flag indicating if the file is original                      | `true`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `_id`        | Record ID                                                    | `a0b0b19a-d526-4xc07-ae51-0xxxxxx`                                                                                                                                                                                                                                                                                                                                                                                                         |
| `url`        | URL of the uploaded file                                     | `https://cdn.pixelbin.io/v2/user-e26cf3/original/testfile.jpeg`                                                                                                                                                                                                                                                                                                                                                                            |

#### Example Usage

##### Uploading a Buffer

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

# Create a config with your API_TOKEN
config = PixelbinConfig(
    {
        "domain": "https://api.pixelbin.io",
        "apiSecret": "API_TOKEN",
    }
)

# Create a PixelBin client instance
pixelbin = PixelbinClient(config=config)

# Sync method call
try:
    # Read the file into a buffer
    with open("myimage.png", "rb") as f:
        buffer = f.read()

    result = pixelbin.uploader.upload(
        file=buffer,
        name="myimage",
        path="folder",
        format="png",
        tags=[],
        metadata={},
        overwrite=False,
        filenameOverride=True,
        access="public-read",
        uploadOptions={
            "chunkSize": 5 * 1024 * 1024,   # 5MB
            "concurrency": 2,                # 2 concurrent chunk uploads
            "maxRetries": 1,                # 1 retry for errors that can be retried
            "exponentialFactor": 2,         # Exponential factor for retries
        }
    )
    print(result["url"])
    # "https://cdn.pixelbin.io/v2/mycloudname/original/folder/myimage.png"
except Exception as e:
    print(e)

# Async method call
try:
    # Read the file into a buffer
    with open("myimage.png", "rb") as f:
        buffer = f.read()

    result = asyncio.get_event_loop().run_until_complete(pixelbin.uploader.uploadAsync(
        file=buffer,
        name="myimage",
        path="folder",
        format="png",
        tags=[],
        metadata={},
        overwrite=False,
        filenameOverride=True,
        access="public-read",
        uploadOptions={
            "chunkSize": 5 * 1024 * 1024,  # 5MB
            "concurrency": 2,                # 2 concurrent chunk uploads
            "maxRetries": 1,                # 1 retry for errors that can be retried
            "exponentialFactor": 2,         # Exponential factor for retries
        }
    ))
    print(result["url"])
    # "https://cdn.pixelbin.io/v2/mycloudname/original/folder/myimage.png"
except Exception as e:
    print(e)

```

##### Uploading a Stream

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

# Create a config with your API_TOKEN
config = PixelbinConfig(
    {
        "domain": "https://api.pixelbin.io",
        "apiSecret": "API_TOKEN",
    }
)

# Create a PixelBin client instance
pixelbin = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.uploader.upload(
        file=open("myimage.png", "rb"), # Open the file as a stream
        name="myimage",
        path="folder",
        format="png",
        tags=[],
        metadata={},
        overwrite=False,
        filenameOverride=True,
        access="public-read",
        uploadOptions={
            "chunkSize": 5 * 1024 * 1024,   # 5MB
            "concurrency": 2,                # 2 concurrent chunk uploads
            "maxRetries": 1,                # 1 retry for errors that can be retried
            "exponentialFactor": 2,         # Exponential factor for retries
        }
    )
    print(result["url"])
    # "https://cdn.pixelbin.io/v2/mycloudname/original/folder/myimage.png"
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.get_event_loop().run_until_complete(pixelbin.uploader.uploadAsync(
        file=open("myimage.png", "rb"), # Open the file as a stream
        name="myimage",
        path="folder",
        format="png",
        tags=[],
        metadata={},
        overwrite=False,
        filenameOverride=True,
        access="public-read",
        uploadOptions={
            "chunkSize": 5 * 1024 * 1024,   # 5MB
            "concurrency": 2,                # 2 concurrent chunk uploads
            "maxRetries": 1,                # 1 retry for errors that can be retried
            "exponentialFactor": 2,         # Exponential factor for retries
        }
    ))
    print(result["url"])
    # "https://cdn.pixelbin.io/v2/mycloudname/original/folder/myimage.png"
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

## Usage with proxy

In case you are using a proxy, you can set `trust_env` to `True` in the `httpClientOptions` object in the `PixelbinConfig` object.
The SDK will trust the environment settings for proxy configuration or ~/.netrc file if present.

#### Quick Example

```python
import asyncio

from pixelbin import PixelbinClient, PixelbinConfig

# create client with your API_TOKEN
config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_TOKEN",
    "options": {
        "httpClientOptions": {
            "trust_env": True
        }
    }
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

## Documentation

-   [API docs](documentation/platform/README.md)
