# Pixelbin Backend SDK for Python

Pixelbin Backend SDK for python helps you integrate the core Pixelbin features with your application.

## Getting Started

Getting started with Pixelbin Backend SDK for Python

### Installation

```
pip install pixelbin
```

______________________________________________________________________

### Initialize client

```python
from pixelbin import PixelbinClient, PixelbinConfig

# Create a config with you API_TOKEN
config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_TOKEN",
})

# Create a pixelbin instance
pixelbin = PixelbinClient(config=config)
```

Note: You will need an API token to authenticate your requests. Follow the Pixelbin Create Token guide to generate one: [Create Token](https://www.pixelbin.io/docs/tokens/create-token/).

## Predictions API

PixelBin's Prediction APIs offer a suite of smart, AI-powered image editing tools designed to streamline your media workflow. These APIs enable you to transform, organize, and enhance images seamlessly within your application or system.

This SDK offers a convenient wrapper around the Prediction API, allowing developers to easily create, track, and manage prediction jobs using async/await. It simplifies image upload, processing, and retrieval within Python applications.

For a broader overview, see the official docs: [Prediction APIs](https://www.pixelbin.io/docs/explore/).

### create

Initiate a prediction job using the prediction model name (for example, `erase_bg`) and input fields as per the model's input schema. Optionally pass a `webhook` URL to receive async notifications.

| Argument | Type | Required | Description |
| --------- | ------ | -------- | ---------------------------------------------------- |
| `name` | `str` | yes | Name of the prediction model, e.g. `erase_bg`. |
| `input` | `dict` | yes | Input fields as per the model input schema. |
| `webhook` | `str` | no | Optional webhook URL to receive async notifications. |

```python
from pixelbin import PixelbinClient, PixelbinConfig
import asyncio

pixelbin = PixelbinClient(config=PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_TOKEN",
}))

# Sync:
job = pixelbin.predictions.create(
    name="erase_bg",
    input={
        # Provide files as bytes or file-like streams; URLs are also accepted as strings
        "image": open("/path/to/image.jpeg", "rb").read(),
        "industry_type": "general",
        "quality_type": "original",
        "shadow": "false",
        "refine": "true",
    },
    webhook="https://example.com/webhook",
)
# job["_id"] can be used to check status

# Async:
async def run():
    job_async = await pixelbin.predictions.createAsync(
        name="erase_bg",
        input={
            "image": open("/path/to/image.jpeg", "rb").read(),
            "industry_type": "general",
            "quality_type": "original",
            "shadow": "false",
            "refine": "true",
        },
        webhook="https://example.com/webhook",
    )
    print(job_async["_id"])

asyncio.get_event_loop().run_until_complete(run())
```

#### Returns

`dict`

On Creation:

| Property | Description | Example |
| ----------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `input` (dict) | Model input | `{ "image": "https://delivery.pixelbin.io/predictions/inputs/erase/bg/0198f54a-cc84-7ccc-b31f-18dd0a5b0f01/image/0.jpeg", ... }` |
| `status` (str) | Current job status | `ACCEPTED` |
| `urls.get` (str) | URL to fetch job details | `https://api.pixelbin.io/service/platform/transformation/v1.0/predictions/erase--bg--0198f54a-cc84-7ccc-b31f-18dd0a5b0f01` |
| `orgId` (int) | Organization id | `402162` |
| `retention` (str) | Output retention period | `30d` |
| `createdAt` (str) | Job creation timestamp (ISO 8601) | `2025-08-29T10:06:16.708Z` |
| `_id` (str) | Prediction request id | `erase--bg--0198f54a-cc84-7ccc-b31f-18dd0a5b0f01` |

On Error:

| Property | Description | Example |
| ----------------- | ----------------- | -------------------------------------------------- |
| `message` (str) | Error message | `Usage Limit Exceeded` |
| `status` (int) | HTTP status code | `403` |
| `errorCode` (str) | Error code | `JR-1000` |
| `exception` (str) | Exception name | `UsageBlockedError` |
| `info` (str) | Help link | `https://fynd.engineering/erasebg/docs/error/1000` |

### get

Fetch the prediction by request ID (job.\_id).

| Argument | Type | Required | Description |
| ------------ | ----- | -------- | ---------------------------------------------------------- |
| `request_id` | `str` | yes | Prediction request ID returned by `create` (`job["_id"]`). |

```python
# Sync:
details = pixelbin.predictions.get(job["_id"])  # string only
if details.get("status") == "SUCCESS":
    print(details.get("output"))

# Async:
import asyncio

async def run():
    details_async = await pixelbin.predictions.getAsync(job["_id"])
    if details_async.get("status") == "SUCCESS":
        print(details_async.get("output"))

asyncio.get_event_loop().run_until_complete(run())
```

#### Returns

`dict`

On Success:

| Property | Description | Example |
| ----------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `input` (dict) | Model input | `{ "image": "https://delivery.pixelbin.io/predictions/inputs/erase/bg/0198f54a-cc84-7ccc-b31f-18dd0a5b0f01/image/0.jpeg", ... }` |
| `status` (str) | Final job status | `SUCCESS` |
| `urls.get` (str) | URL to fetch job details | `https://api.pixelbin.io/service/platform/transformation/v1.0/predictions/erase--bg--0198f54a-cc84-7ccc-b31f-18dd0a5b0f01` |
| `orgId` (int) | Organization id | `402162` |
| `retention` (str) | Output retention period | `30d` |
| `createdAt` (str) | Job creation timestamp (ISO 8601) | `2025-08-29T10:06:16.708Z` |
| `_id` (str) | Prediction request id | `erase--bg--0198f54a-cc84-7ccc-b31f-18dd0a5b0f01` |
| `consumedCredits` (int) | Credits consumed | `1` |
| `output` (list[str]) | Result URLs | `["https://delivery.pixelbin.io/predictions/outputs/30d/erase/bg/0198f54a-cc84-7ccc-b31f-18dd0a5b0f01/result_0.png"]` |

On Failure:

| Property | Description | Example |
| ----------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `input` (dict) | Model input | `{ "industry_type": "general", "quality_type": "original", "shadow": False, "refine": True }` |
| `status` (str) | Final job status | `FAILURE` |
| `urls.get` (str) | URL to fetch job details | `https://api.pixelbin.io/service/platform/transformation/v1.0/predictions/erase--bg--0198f54b-8d2e-7ccc-b31f-2a2f33cb7365` |
| `orgId` (int) | Organization id | `402162` |
| `retention` (str) | Output retention period | `30d` |
| `createdAt` (str) | Job creation timestamp (ISO 8601) | `2025-08-29T10:07:06.030Z` |
| `_id` (str) | Prediction request id | `erase--bg--0198f54b-8d2e-7ccc-b31f-2a2f33cb7365` |
| `error` (str) | Error message | `image not found` |

### wait

Wait until the prediction completes.

| Argument | Type | Required | Description |
| ------------ | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `request_id` | `str` | yes | Prediction request ID to poll until status is `SUCCESS` or `FAILURE`. |
| `options` | `dict` | no | Polling options: `maxAttempts` (int, default 150, range 1-150), `retryFactor` (float, default 1, range 1-3), `retryInterval` (seconds, float, default 4.0, range 1-60). |

```python
# Sync:
result = pixelbin.predictions.wait(job["_id"])  # string only

result_quick = pixelbin.predictions.wait(job["_id"], {
    "maxAttempts": 30,
    "retryFactor": 1,
    "retryInterval": 1.0,
})

print(result.get("status"))  # Prediction status
print(result.get("output"))  # Prediction output

# Async:
import asyncio

async def run():
    result_async = await pixelbin.predictions.waitAsync(job["_id"], {
        "maxAttempts": 30,
        "retryFactor": 1,
        "retryInterval": 1.0,
    })
    print(result_async.get("status"), result_async.get("output"))

asyncio.get_event_loop().run_until_complete(run())
```

#### Returns

`dict`

Same as `get` above. `wait` resolves to the final prediction object (either SUCCESS or FAILURE).

### create_and_wait

Create a prediction and wait until it completes. Returns the final result.

| Argument | Type | Required | Description |
| --------- | ------ | -------- | -------------------------------------------------------------- |
| `name` | `str` | yes | Prediction name in `plugin_operation` format, e.g. `erase_bg`. |
| `input` | `dict` | yes | Input fields as per the model input schema. |
| `webhook` | `str` | no | Optional webhook URL. |
| `options` | `dict` | no | Same options as in `wait`. |

```python
# Sync:
result = pixelbin.predictions.create_and_wait(
    name="erase_bg",
    input={"image": open("/path/to/image.jpeg", "rb").read()},
    options={"maxAttempts": 60, "retryFactor": 1, "retryInterval": 2.0},
)

# Async:
import asyncio

async def run():
    result_async = await pixelbin.predictions.create_and_waitAsync(
        name="erase_bg",
        input={"image": open("/path/to/image.jpeg", "rb").read()},
        options={"maxAttempts": 60, "retryFactor": 1, "retryInterval": 2.0},
    )
    print(result_async.get("status"))

asyncio.get_event_loop().run_until_complete(run())
```

#### Returns

`dict`

Same as `get` above. `create_and_wait` resolves to the final prediction object (either SUCCESS or FAILURE).

### list

Fetch the list of available prediction models.

```python
# Sync:
items = pixelbin.predictions.list()
print(len(items) if isinstance(items, list) else 0)

# Async:
import asyncio

async def run():
    items_async = await pixelbin.predictions.listAsync()
    print(len(items_async) if isinstance(items_async, list) else 0)

asyncio.get_event_loop().run_until_complete(run())
```

#### Returns

`list[dict]`

Each item:

| Property | Description | Example |
| ------------------- | ----------------------------------------- | --------------------------- |
| `name` (str) | Unique identifier of the prediction model | `erase_bg` |
| `displayName` (str) | Human readable name of the model | `Erase Background` |
| `description` (str) | Short model description | `Removes image background.` |

### get_schema

Fetch the input schema for a specific prediction model by its name.

| Argument | Type | Required | Description |
| -------- | ----- | -------- | --------------------------------- |
| `name` | `str` | yes | Prediction name, e.g. `erase_bg`. |

```python
# Sync:
schema = pixelbin.predictions.get_schema("erase_bg")
print(schema.get("name") if isinstance(schema, dict) else None)

# Async:
import asyncio

async def run():
    schema_async = await pixelbin.predictions.get_schemaAsync("erase_bg")
    print(schema_async.get("name") if isinstance(schema_async, dict) else None)

asyncio.get_event_loop().run_until_complete(run())
```

#### Returns

`dict`

| Property | Description | Example |
| ------------------- | ---------------------------------------------- | --------------------------- |
| `name` (str) | Model name | `erase_bg` |
| `displayName` (str) | Human readable name | `Erase Background` |
| `description` (str) | Model description | `Removes image background.` |
| `input` (dict) | JSON Schema for model inputs (varies by model) | `{ ... }` |

Fields inside `input.image` (varies by model):

| Property | Description | Example |
| ----------------------------------- | ------------------------------------------------ | ---------------------------------- |
| `oneOf` (list) | Supported input types (e.g., URL or file upload) | `[ ... ]` |
| `supportedContentTypes` (list[str]) | Supported MIME types | `["image/png", "image/jpeg", ...]` |
| `imageValidation.maxWidth` (int) | Max image width in pixels | `10000` |
| `imageValidation.maxHeight` (int) | Max image height in pixels | `10000` |
| `imageValidation.maxSize` (int) | Max image size in bytes | `26214400` |

## Examples

### 1. Implementation using `create`, `get` and `wait` method

Sync version:

```python
from pixelbin import PixelbinClient, PixelbinConfig

def generate_image():
    pixelbin = PixelbinClient(
        config=PixelbinConfig({
            "domain": "https://api.pixelbin.io",
            "apiSecret": os.getenv("PIXELBIN_API_TOKEN") or "API_TOKEN",
        })
    )

    try:
        # 1) Create prediction
        job = pixelbin.predictions.create(
            name="erase_bg",
            input={
                "image": "https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg",
                "industry_type": "general",
                "quality_type": "original",
                "shadow": False,
                "refine": True,
            },
            # webhook="https://example.com/webhook",  # optional
        )
        print("Created:", job.get("_id"), job.get("status"))

        # 2) get job details
        details = pixelbin.predictions.get(job["_id"])  # string only
        print("Details:", details.get("status"))

        # 3) Wait for completion
        result = pixelbin.predictions.wait(job["_id"])  # string only
        print("Final:", result.get("status"), result.get("output"))
    except Exception as err:
        print("Error:", err)

if __name__ == "__main__":
    import os
    generate_image()
```

Async version:

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

async def generate_image_async():
    pixelbin = PixelbinClient(
        config=PixelbinConfig({
            "domain": "https://api.pixelbin.io",
            "apiSecret": os.getenv("PIXELBIN_API_TOKEN") or "API_TOKEN",
        })
    )

    try:
        # 1) Create prediction (async)
        job = await pixelbin.predictions.createAsync(
            name="erase_bg",
            input={
                "image": "https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg",
                "industry_type": "general",
                "quality_type": "original",
                "shadow": False,
                "refine": True,
            },
            # webhook="https://example.com/webhook",  # optional
        )
        print("Created:", job.get("_id"), job.get("status"))

        # 2) get job details (async)
        details = await pixelbin.predictions.getAsync(job["_id"])  # string only
        print("Details:", details.get("status"))

        # 3) Wait for completion (async)
        result = await pixelbin.predictions.waitAsync(job["_id"])  # string only
        print("Final:", result.get("status"), result.get("output"))
    except Exception as err:
        print("Error:", err)

if __name__ == "__main__":
    import os
    asyncio.get_event_loop().run_until_complete(generate_image_async())
```

### 2. Implementation with `create_and_wait` method

Sync version:

```python
from pixelbin import PixelbinClient, PixelbinConfig

def generate_image():
    pixelbin = PixelbinClient(
        config=PixelbinConfig({
            "domain": "https://api.pixelbin.io",
            "apiSecret": os.getenv("PIXELBIN_API_TOKEN") or "API_TOKEN",
        })
    )

    try:
        result = pixelbin.predictions.create_and_wait(
            name="erase_bg",
            input={
                "image": "https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg",
                "industry_type": "general",
                "quality_type": "original",
                "shadow": False,
                "refine": True,
            },
            # webhook="https://example.com/webhook",  # optional
        )
        print(result)  # { status, output, ... }
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    import os
    generate_image()
```

Async version:

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

async def generate_image_async():
    pixelbin = PixelbinClient(
        config=PixelbinConfig({
            "domain": "https://api.pixelbin.io",
            "apiSecret": os.getenv("PIXELBIN_API_TOKEN") or "API_TOKEN",
        })
    )

    try:
        result = await pixelbin.predictions.create_and_waitAsync(
            name="erase_bg",
            input={
                "image": "https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg",
                "industry_type": "general",
                "quality_type": "original",
                "shadow": False,
                "refine": True,
            },
            # webhook="https://example.com/webhook",  # optional
        )
        print(result)  # { status, output, ... }
    except Exception as error:
        print("Error:", error)

if __name__ == "__main__":
    import os
    asyncio.get_event_loop().run_until_complete(generate_image_async())
```

## Uploader

### upload

Uploads a file to PixelBin with greater control over the upload process.

#### Arguments

| Argument | Type | Required | Description |
| ------------------- | ----------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `file` | `bytes` or `io.BufferedIOBase` | yes | The file to be uploaded. |
| `name` | `str` | no | Name of the file. |
| `path` | `str` | no | Path of the containing folder. |
| `format` | `str` | no | Format of the file. |
| `access` | [AccessEnum](./documentation/platform/ASSETS.md#accessenum) | no | Access level of the asset, can be either `'public-read'` or `'private'`. |
| `tags` | `list[str]` | no | Tags associated with the file. |
| `metadata` | `dict` | no | Metadata associated with the file. |
| `overwrite` | `bool` | no | Overwrite flag. If set to `True`, will overwrite any file that exists with the same path, name, and type. Defaults to `False`. |
| `filenameOverride` | `bool` | no | If set to `True`, will add unique characters to the name if an asset with the given name already exists. If the overwrite flag is set to `True`, preference will be given to the overwrite flag. If both are set to `False`, an error will be raised. |
| `expiry` | `int` | no | Expiry time in seconds for the underlying signed URL. Defaults to 3000 seconds. |
| `uploadOptions` | `dict` | no | Additional options for fine-tuning the upload process. Default: `{ chunk_size: 10 * 1024 * 1024, max_retries: 2, concurrency: 3, exponential_factor: 2 }`. |
| `chunkSize` | `int` | no | Size of each chunk to upload. Default is 10 megabytes. |
| `maxRetries` | `int` | no | Maximum number of retries if an upload fails. Default is 2 retries. |
| `concurrency` | `int` | no | Number of concurrent chunk upload tasks. Default is 3 concurrent chunk uploads. |
| `exponentialFactor` | `int` | no | The exponential factor for retry delay. Default is 2. |

#### Returns

`dict`: On success, returns a dictionary containing the details of the uploaded file.

| Property | Description | Example |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `orgId` | Organization ID | `5320086` |
| `type` | Type of the uploaded entity | `file` |
| `name` | Name of the file | `testfile.jpeg` |
| `path` | Path of the containing folder | `/path/to/image.jpeg` |
| `fileId` | ID of the file | `testfile.jpeg` |
| `access` | Access level of the asset, can be `public-read` or `private` | `public-read` |
| `tags` | Tags associated with the file | `["tag1", "tag2"]` |
| `metadata` | Metadata associated with the file | `{"source":"", "publicUploadId":""}` |
| `format` | File format | `jpeg` |
| `assetType` | Type of asset | `image` |
| `size` | File size (in bytes) | `37394` |
| `width` | File width (in pixels) | `720` |
| `height` | File height (in pixels) | `450` |
| `context` | File metadata and additional context | `{"steps":[],"req":{"headers":{},"query":{}},"meta":{"format":"png","size":195337,"width":812,"height":500,"space":"srgb","channels":4,"depth":"uchar","density":144,"isProgressive":false,"resolutionUnit":"inch","hasProfile":true,"hasAlpha":true,"extension":"jpeg","contentType":"image/png","assetType":"image","isImageAsset":true,"isAudioAsset":false,"isVideoAsset":false,"isRawAsset":false,"isTransformationSupported":true}}` |
| `isOriginal` | Flag indicating if the file is original | `true` |
| `_id` | Record ID | `a0b0b19a-d526-4xc07-ae51-0xxxxxx` |
| `url` | URL of the uploaded file | `https://cdn.pixelbin.io/v2/user-e26cf3/original/testfile.jpeg` |

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

| Parameter | Description | Example |
| ---------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `url` (string) | A valid Pixelbin URL to be signed | `https://cdn.pixelbin.io/v2/dummy-cloudname/original/__playground/playground-default.jpeg` |
| `expiry_seconds` (int) | Number of seconds the signed URL should be valid for | `20` |
| `access_key` (string) | Access key of the token used for signing | `6227274d-92c9-4b74-bef8-2528542516d8` |
| `token` (string) | Value of the token used for signing | `dummy-token` |

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

| parameter | description | example |
| ----------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| `url` (string) | A valid Pixelbin URL | `https://cdn.pixelbin.io/v2/your-cloud-name/z-slug/t.resize(h:100,w:200)~t.flip()/path/to/image.jpeg` |
| `opts` (Object) | Options for the conversion | Default: `{ isCustomDomain: False }` |
| `opts.is_custom_domain` | Indicates if the URL belongs to a custom domain (default: `False`) |

**Returns**:

| Property | Description | Example |
| ------------------------- | ---------------------------------------------------- | ------------------------------------- |
| `baseURL` (string) | Base path of the URL | `https://cdn.pixelbin.io` |
| `filePath` (string) | Path to the file on Pixelbin storage | `/path/to/image.jpeg` |
| `version` (string) | Version of the URL | `v2` |
| `cloudName` (string) | Cloud name from the URL | `your-cloud-name` |
| `transformations` (array) | A list of transformation objects | `[{ "plugin": "t", "name": "flip" }]` |
| `zone` (string) | Zone slug from the URL | `z-slug` |
| `pattern` (string) | Transformation pattern extracted from the URL | `t.resize(h:100,w:200)~t.flip()` |
| `worker` (boolean) | Indicates if the URL is a URL Translation Worker URL | `False` |
| `workerPath` (string) | Input path to a URL Translation Worker | `resize:w200,h400/folder/image.jpeg` |
| `options` (Object) | Query parameters added, such as "dpr" and "f_auto" | `{ dpr: 2.5, f_auto: True}` |

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

| Property | Description | Example |
| -------------------------- | ---------------------------------------------------- | ------------------------------------- |
| `cloudName` (string) | The cloudname extracted from the URL | `your-cloud-name` |
| `zone` (string) | 6 character zone slug | `z-slug` |
| `version` (string) | CDN API version | `v2` |
| `transformations` (array) | Extracted transformations from the URL | `[{ "plugin": "t", "name": "flip" }]` |
| `filePath` (string) | Path to the file on Pixelbin storage | `/path/to/image.jpeg` |
| `baseUrl` (string) | Base URL | `https://cdn.pixelbin.io/` |
| `isCustomDomain` (boolean) | Indicates if the URL is for a custom domain | `False` |
| `worker` (boolean) | Indicates if the URL is a URL Translation Worker URL | `False` |
| `workerPath` (string) | Input path to a URL Translation Worker | `resize:w200,h400/folder/image.jpeg` |
| `options` (Object) | Query parameters added, such as "dpr" and "f_auto" | `{ "dpr": "2.0", "f_auto": True }` |

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

- [API docs](documentation/platform/README.md)
