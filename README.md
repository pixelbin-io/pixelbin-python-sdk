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

// create client with your API_TOKEN
config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_TOKEN",
})

// Create a pixelbin instance
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
