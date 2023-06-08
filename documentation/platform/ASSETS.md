##### [Back to Pixelbin API docs](./README.md)

## Assets Methods

Asset Uploader Service

-   [fileUpload](#fileupload)
-   [urlUpload](#urlupload)
-   [createSignedUrl](#createsignedurl)
-   [listFiles](#listfiles)
-   [listFilesPaginator](#listfilespaginator)
-   [getFileById](#getfilebyid)
-   [getFileByFileId](#getfilebyfileid)
-   [updateFile](#updatefile)
-   [deleteFile](#deletefile)
-   [deleteFiles](#deletefiles)
-   [createFolder](#createfolder)
-   [getFolderDetails](#getfolderdetails)
-   [updateFolder](#updatefolder)
-   [deleteFolder](#deletefolder)
-   [getFolderAncestors](#getfolderancestors)
-   [addCredentials](#addcredentials)
-   [updateCredentials](#updatecredentials)
-   [deleteCredentials](#deletecredentials)
-   [addPreset](#addpreset)
-   [getPresets](#getpresets)
-   [updatePreset](#updatepreset)
-   [deletePreset](#deletepreset)
-   [getPreset](#getpreset)
-   [getDefaultAssetForPlayground](#getdefaultassetforplayground)
-   [getModules](#getmodules)
-   [getModule](#getmodule)

## Methods with example and description

### fileUpload

**Summary**: Upload File

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.fileUpload(
        file=open("your-file-path", "rb"),
        path="path/to/containing/folder",
        name="filename",
        access="public-read",
        tags=["tag1","tag2"],
        metadata={},
        overwrite=False,
        filenameOverride=True)
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.fileUploadAsync(
        file=open("your-file-path", "rb"),
        path="path/to/containing/folder",
        name="filename",
        access="public-read",
        tags=["tag1","tag2"],
        metadata={},
        overwrite=False,
        filenameOverride=True))
    # use result
except Exception as e:
    print(e)

```

| Argument         | Type       | Required | Description                                                                                                                                                                                                                      |
| ---------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| file             | FileIO     | yes      | Asset file                                                                                                                                                                                                                       |
| path             | str        | no       | Path where you want to store the asset. Path of containing folder                                                                                                                                                                |
| name             | str        | no       | Name of the asset, if not provided name of the file will be used. Note - The provided name will be slugified to make it URL safe                                                                                                 |
| access           | AccessEnum | no       | Access level of asset, can be either `public-read` or `private`                                                                                                                                                                  |
| tags             | List[str]  | no       | Asset tags                                                                                                                                                                                                                       |
| metadata         | Any        | no       | Asset related metadata                                                                                                                                                                                                           |
| overwrite        | bool       | no       | Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`.                                                                                                         |
| filenameOverride | bool       | no       | If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. |

Upload File to Pixelbin

_Returned Response:_

[UploadResponse](#uploadresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "asset",
    "path": "dir",
    "fileId": "dir/asset",
    "format": "jpeg",
    "size": 1000,
    "access": "private",
    "isActive": true,
    "tags": ["tag1", "tag2"],
    "metadata": {
        "key": "value"
    },
    "url": "https://domain.com/filename.jpeg"
}
```

</details>

### urlUpload

**Summary**: Upload Asset with url

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.urlUpload(
        url="www.dummy.com/image.png",
        path="path/to/containing/folder",
        name="filename",
        access="public-read",
        tags=["tag1","tag2"],
        metadata={},
        overwrite=False,
        filenameOverride=True)
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.urlUploadAsync(
        url="www.dummy.com/image.png",
        path="path/to/containing/folder",
        name="filename",
        access="public-read",
        tags=["tag1","tag2"],
        metadata={},
        overwrite=False,
        filenameOverride=True))
    # use result
except Exception as e:
    print(e)

```

| Argument         | Type       | Required | Description                                                                                                                                                                                                                      |
| ---------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| url              | str        | yes      | Asset URL                                                                                                                                                                                                                        |
| path             | str        | no       | Path where you want to store the asset. Path of containing folder.                                                                                                                                                               |
| name             | str        | no       | Name of the asset, if not provided name of the file will be used. Note - The provided name will be slugified to make it URL safe                                                                                                 |
| access           | AccessEnum | no       | Access level of asset, can be either `public-read` or `private`                                                                                                                                                                  |
| tags             | List[str]  | no       | Asset tags                                                                                                                                                                                                                       |
| metadata         | Any        | no       | Asset related metadata                                                                                                                                                                                                           |
| overwrite        | bool       | no       | Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`.                                                                                                         |
| filenameOverride | bool       | no       | If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. |

Upload Asset with url

_Returned Response:_

[UploadResponse](#uploadresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "asset",
    "path": "dir",
    "fileId": "dir/asset",
    "format": "jpeg",
    "size": 1000,
    "access": "private",
    "isActive": true,
    "tags": ["tag1", "tag2"],
    "metadata": {
        "key": "value"
    },
    "url": "https://domain.com/filename.jpeg"
}
```

</details>

### createSignedUrl

**Summary**: S3 Signed URL upload

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.createSignedUrl(
        name="filename",
        path="path/to/containing/folder",
        format="jpeg",
        access="public-read",
        tags=["tag1","tag2"],
        metadata={},
        overwrite=False,
        filenameOverride=True)
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.createSignedUrlAsync(
        name="filename",
        path="path/to/containing/folder",
        format="jpeg",
        access="public-read",
        tags=["tag1","tag2"],
        metadata={},
        overwrite=False,
        filenameOverride=True))
    # use result
except Exception as e:
    print(e)

```

| Argument         | Type       | Required | Description                                                                                                                                                                                                                      |
| ---------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name             | str        | no       | name of the file                                                                                                                                                                                                                 |
| path             | str        | no       | Path of containing folder.                                                                                                                                                                                                       |
| format           | str        | no       | Format of the file                                                                                                                                                                                                               |
| access           | AccessEnum | no       | Access level of asset, can be either `public-read` or `private`                                                                                                                                                                  |
| tags             | List[str]  | no       | Tags associated with the file.                                                                                                                                                                                                   |
| metadata         | Any        | no       | Metadata associated with the file.                                                                                                                                                                                               |
| overwrite        | bool       | no       | Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`.                                                                                                         |
| filenameOverride | bool       | no       | If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. |

For the given asset details, a S3 signed URL will be generated,
which can be then used to upload your asset.

_Returned Response:_

[SignedUploadResponse](#signeduploadresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "s3PresignedUrl": {
        "url": "https://domain.com/xyz",
        "fields": {
            "field1": "value",
            "field2": "value"
        }
    }
}
```

</details>

### listFiles

**Summary**: List and search files and folders.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.listFiles(
        name="cat",
        path="cat-photos",
        format="jpeg",
        tags=["cats","animals"],
        onlyFiles="false",
        onlyFolders="false",
        pageNo=1,
        pageSize=10,
        sort="name")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.listFilesAsync(
        name="cat",
        path="cat-photos",
        format="jpeg",
        tags=["cats","animals"],
        onlyFiles="false",
        onlyFolders="false",
        pageNo=1,
        pageSize=10,
        sort="name"))
    # use result
except Exception as e:
    print(e)

```

| Argument    | Type      | Required | Description                                                                  |
| ----------- | --------- | -------- | ---------------------------------------------------------------------------- |
| name        | str       | no       | Find items with matching name                                                |
| path        | str       | no       | Find items with matching path                                                |
| format      | str       | no       | Find items with matching format                                              |
| tags        | List[str] | no       | Find items containing these tags                                             |
| onlyFiles   | bool      | no       | If true will fetch only files                                                |
| onlyFolders | bool      | no       | If true will fetch only folders                                              |
| pageNo      | int       | no       | Page No.                                                                     |
| pageSize    | int       | no       | Page Size                                                                    |
| sort        | str       | no       | Key to sort results by. A "-" suffix will sort results in descending orders. |

List all files and folders in root folder. Search for files if name is provided. If path is provided, search in the specified path.

_Returned Response:_

[ListFilesResponse](#listfilesresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "items": [
        {
            "_id": "dummy-uuid",
            "name": "dir",
            "type": "folder"
        },
        {
            "_id": "dummy-uuid",
            "name": "asset2",
            "type": "file",
            "path": "dir",
            "fileId": "dir/asset2",
            "format": "jpeg",
            "size": 1000,
            "access": "private"
        },
        {
            "_id": "dummy-uuid",
            "name": "asset1",
            "type": "file",
            "path": "dir",
            "fileId": "dir/asset1",
            "format": "jpeg",
            "size": 1000,
            "access": "private"
        }
    ],
    "page": {
        "type": "number",
        "size": 4,
        "current": 1,
        "hasNext": false
    }
}
```

</details>

### getFileById

**Summary**: Get file details with \_id

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getFileById(
        _id="c9138153-94ea-4dbe-bea9-65d43dba85ae")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getFileByIdAsync(
        _id="c9138153-94ea-4dbe-bea9-65d43dba85ae"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description  |
| -------- | ---- | -------- | ------------ |
| \_id     | str  | yes      | \_id of File |

_Returned Response:_

[FilesResponse](#filesresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "asset",
    "path": "dir",
    "fileId": "dir/asset",
    "format": "jpeg",
    "size": 1000,
    "access": "private",
    "isActive": true,
    "tags": ["tag1", "tag2"],
    "metadata": {
        "key": "value"
    },
    "url": "https://domain.com/filename.jpeg"
}
```

</details>

### getFileByFileId

**Summary**: Get file details with fileId

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getFileByFileId(
        fileId="path/to/file/name")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getFileByFileIdAsync(
        fileId="path/to/file/name"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description                              |
| -------- | ---- | -------- | ---------------------------------------- |
| fileId   | str  | yes      | Combination of `path` and `name` of file |

_Returned Response:_

[FilesResponse](#filesresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "asset",
    "path": "dir",
    "fileId": "dir/asset",
    "format": "jpeg",
    "size": 1000,
    "access": "private",
    "isActive": true,
    "tags": ["tag1", "tag2"],
    "metadata": {
        "key": "value"
    },
    "url": "https://domain.com/filename.jpeg"
}
```

</details>

### updateFile

**Summary**: Update file details

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.updateFile(
        fileId="path/to/file/name",
        name="asset",
        path="dir",
        access="private",
        isActive=False,
        tags=["tag1","tag2"],
        metadata={"key":"value"})
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.updateFileAsync(
        fileId="path/to/file/name",
        name="asset",
        path="dir",
        access="private",
        isActive=False,
        tags=["tag1","tag2"],
        metadata={"key":"value"}))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type      | Required | Description                                                     |
| -------- | --------- | -------- | --------------------------------------------------------------- |
| fileId   | str       | yes      | Combination of `path` and `name`                                |
| name     | str       | no       | Name of the file                                                |
| path     | str       | no       | path of containing folder.                                      |
| access   | str       | no       | Access level of asset, can be either `public-read` or `private` |
| isActive | bool      | no       | Whether the file is active                                      |
| tags     | List[str] | no       | Tags associated with the file                                   |
| metadata | Any       | no       | Metadata associated with the file                               |

_Returned Response:_

[FilesResponse](#filesresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "asset",
    "path": "dir",
    "fileId": "dir/asset",
    "format": "jpeg",
    "size": 1000,
    "access": "private",
    "isActive": true,
    "tags": ["tag1", "tag2"],
    "metadata": {
        "key": "value"
    },
    "url": "https://domain.com/filename.jpeg"
}
```

</details>

### deleteFile

**Summary**: Delete file

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.deleteFile(
        fileId="path/to/file/name")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.deleteFileAsync(
        fileId="path/to/file/name"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description                      |
| -------- | ---- | -------- | -------------------------------- |
| fileId   | str  | yes      | Combination of `path` and `name` |

_Returned Response:_

[FilesResponse](#filesresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "asset",
    "path": "dir",
    "fileId": "dir/asset",
    "format": "jpeg",
    "size": 1000,
    "access": "private",
    "isActive": true,
    "tags": ["tag1", "tag2"],
    "metadata": {
        "key": "value"
    },
    "url": "https://domain.com/filename.jpeg"
}
```

</details>

### deleteFiles

**Summary**: Delete multiple files

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.deleteFiles(
        ids=["_id_1","_id_2","_id_3"])
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.deleteFilesAsync(
        ids=["_id_1","_id_2","_id_3"]))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type      | Required | Description                   |
| -------- | --------- | -------- | ----------------------------- |
| ids      | List[str] | yes      | Array of file \_ids to delete |

_Returned Response:_

[List[FilesResponse]](#filesresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
[
    {
        "_id": "dummy-uuid",
        "name": "asset",
        "path": "dir",
        "fileId": "dir/asset",
        "format": "jpeg",
        "size": 1000,
        "access": "private",
        "isActive": true,
        "tags": ["tag1", "tag2"],
        "metadata": {
            "key": "value"
        },
        "url": "https://domain.com/filename.jpeg"
    }
]
```

</details>

### createFolder

**Summary**: Create folder

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.createFolder(
        name="subDir",
        path="dir")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.createFolderAsync(
        name="subDir",
        path="dir"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description                |
| -------- | ---- | -------- | -------------------------- |
| name     | str  | yes      | Name of the folder         |
| path     | str  | no       | path of containing folder. |

Create a new folder at the specified path. Also creates the ancestors if they do not exist.

_Returned Response:_

[FoldersResponse](#foldersresponse)

Success - List of all created folders

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "subDir",
    "path": "dir",
    "isActive": true
}
```

</details>

### getFolderDetails

**Summary**: Get folder details

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getFolderDetails(
        path="dir1/dir2",
        name="dir")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getFolderDetailsAsync(
        path="dir1/dir2",
        name="dir"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description |
| -------- | ---- | -------- | ----------- |
| path     | str  | no       | Folder path |
| name     | str  | no       | Folder name |

Get folder details

_Returned Response:_

[exploreItem](#exploreitem)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
[
    {
        "_id": "dummy-uuid",
        "createdAt": "2022-10-05T10:43:04.117Z",
        "updatedAt": "2022-10-05T10:43:04.117Z",
        "name": "asset2",
        "type": "file",
        "path": "dir",
        "fileId": "dir/asset2",
        "format": "jpeg",
        "size": 1000,
        "access": "private",
        "metadata": {},
        "height": 100,
        "width": 100
    }
]
```

</details>

### updateFolder

**Summary**: Update folder details

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.updateFolder(
        folderId="path/to/folder/name",
        isActive=False)
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.updateFolderAsync(
        folderId="path/to/folder/name",
        isActive=False))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description                      |
| -------- | ---- | -------- | -------------------------------- |
| folderId | str  | yes      | combination of `path` and `name` |
| isActive | bool | no       | whether the folder is active     |

Update folder details. Eg: Soft delete it
by making `isActive` as `false`.
We currently do not support updating folder name or path.

_Returned Response:_

[FoldersResponse](#foldersresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "subDir",
    "path": "dir",
    "isActive": true
}
```

</details>

### deleteFolder

**Summary**: Delete folder

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.deleteFolder(
        _id="c9138153-94ea-4dbe-bea9-65d43dba85ae")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.deleteFolderAsync(
        _id="c9138153-94ea-4dbe-bea9-65d43dba85ae"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description                  |
| -------- | ---- | -------- | ---------------------------- |
| \_id     | str  | yes      | \_id of folder to be deleted |

Delete folder and all its children permanently.

_Returned Response:_

[FoldersResponse](#foldersresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "subDir",
    "path": "dir",
    "isActive": true
}
```

</details>

### getFolderAncestors

**Summary**: Get all ancestors of a folder

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getFolderAncestors(
        _id="c9138153-94ea-4dbe-bea9-65d43dba85ae")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getFolderAncestorsAsync(
        _id="c9138153-94ea-4dbe-bea9-65d43dba85ae"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description        |
| -------- | ---- | -------- | ------------------ |
| \_id     | str  | yes      | \_id of the folder |

Get all ancestors of a folder, using the folder ID.

_Returned Response:_

[GetAncestorsResponse](#getancestorsresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "folder": {
        "_id": "dummy-uuid",
        "name": "subDir",
        "path": "dir1/dir2",
        "isActive": true
    },
    "ancestors": [
        {
            "_id": "dummy-uuid-2",
            "name": "dir1",
            "path": "",
            "isActive": true
        },
        {
            "_id": "dummy-uuid-2",
            "name": "dir2",
            "path": "dir1",
            "isActive": true
        }
    ]
}
```

</details>

### addCredentials

**Summary**: Add credentials for a transformation module.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.addCredentials(
        credentials={"region":"ap-south-1","accessKeyId":"123456789ABC","secretAccessKey":"DUMMY1234567890"},
        pluginId="awsRek")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.addCredentialsAsync(
        credentials={"region":"ap-south-1","accessKeyId":"123456789ABC","secretAccessKey":"DUMMY1234567890"},
        pluginId="awsRek"))
    # use result
except Exception as e:
    print(e)

```

| Argument    | Type | Required | Description                                                 |
| ----------- | ---- | -------- | ----------------------------------------------------------- |
| credentials | Any  | yes      | Credentials of the plugin                                   |
| pluginId    | str  | yes      | Unique identifier for the plugin this credential belongs to |

Add a transformation modules's credentials for an organization.

_Returned Response:_

[AddCredentialsResponse](#addcredentialsresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "123ee789-7ae8-4336-b9bd-e4f33c049002",
    "createdAt": "2022-10-04T09:52:09.545Z",
    "updatedAt": "2022-10-04T09:52:09.545Z",
    "orgId": 23,
    "pluginId": "awsRek"
}
```

</details>

### updateCredentials

**Summary**: Update credentials of a transformation module.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.updateCredentials(
        pluginId="awsRek",
        credentials={"region":"ap-south-1","accessKeyId":"123456789ABC","secretAccessKey":"DUMMY1234567890"})
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.updateCredentialsAsync(
        pluginId="awsRek",
        credentials={"region":"ap-south-1","accessKeyId":"123456789ABC","secretAccessKey":"DUMMY1234567890"}))
    # use result
except Exception as e:
    print(e)

```

| Argument    | Type | Required | Description                                          |
| ----------- | ---- | -------- | ---------------------------------------------------- |
| pluginId    | str  | yes      | ID of the plugin whose credentials are being updated |
| credentials | Any  | yes      | Credentials of the plugin                            |

Update credentials of a transformation module, for an organization.

_Returned Response:_

[AddCredentialsResponse](#addcredentialsresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "123ee789-7ae8-4336-b9bd-e4f33c049002",
    "createdAt": "2022-10-04T09:52:09.545Z",
    "updatedAt": "2022-10-04T09:52:09.545Z",
    "orgId": 23,
    "pluginId": "awsRek"
}
```

</details>

### deleteCredentials

**Summary**: Delete credentials of a transformation module.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.deleteCredentials(
        pluginId="awsRek")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.deleteCredentialsAsync(
        pluginId="awsRek"))
    # use result
except Exception as e:
    print(e)

```

| Argument | Type | Required | Description                                          |
| -------- | ---- | -------- | ---------------------------------------------------- |
| pluginId | str  | yes      | ID of the plugin whose credentials are being deleted |

Delete credentials of a transformation module, for an organization.

_Returned Response:_

[AddCredentialsResponse](#addcredentialsresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "123ee789-7ae8-4336-b9bd-e4f33c049002",
    "createdAt": "2022-10-04T09:52:09.545Z",
    "updatedAt": "2022-10-04T09:52:09.545Z",
    "orgId": 23,
    "pluginId": "awsRek"
}
```

</details>

### addPreset

**Summary**: Add a preset.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.addPreset(
        presetName="p1",
        transformation="t.flip()~t.flop()",
        params={"w":{"type":"integer","default":200},"h":{"type":"integer","default":400}})
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.addPresetAsync(
        presetName="p1",
        transformation="t.flip()~t.flop()",
        params={"w":{"type":"integer","default":200},"h":{"type":"integer","default":400}}))
    # use result
except Exception as e:
    print(e)

```

| Argument       | Type | Required | Description                                    |
| -------------- | ---- | -------- | ---------------------------------------------- |
| presetName     | str  | yes      | Name of the preset                             |
| transformation | str  | yes      | A chain of transformations, separated by `~`   |
| params         | Any  | no       | Parameters object for transformation variables |

Add a preset for an organization.

_Returned Response:_

[AddPresetResponse](#addpresetresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "presetName": "p1",
    "transformation": "t.flip()~t.flop()",
    "params": {
        "w": {
            "type": "integer",
            "default": 200
        },
        "h": {
            "type": "integer",
            "default": 400
        }
    },
    "archived": false
}
```

</details>

### getPresets

**Summary**: Get all presets.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getPresets()
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getPresetsAsync())
    # use result
except Exception as e:
    print(e)

```

Get all presets of an organization.

_Returned Response:_

[AddPresetResponse](#addpresetresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "items": [
        {
            "presetName": "p1",
            "transformation": "t.flip()~t.flop()",
            "params": {
                "w": {
                    "type": "integer",
                    "default": 200
                },
                "h": {
                    "type": "integer",
                    "default": 400
                }
            },
            "archived": true
        }
    ],
    "page": {
        "type": "number",
        "size": 1,
        "current": 1,
        "hasNext": false
    }
}
```

</details>

### updatePreset

**Summary**: Update a preset.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.updatePreset(
        presetName="p1",
        archived=True)
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.updatePresetAsync(
        presetName="p1",
        archived=True))
    # use result
except Exception as e:
    print(e)

```

| Argument   | Type | Required | Description                               |
| ---------- | ---- | -------- | ----------------------------------------- |
| presetName | str  | yes      | Name of the preset to be updated          |
| archived   | bool | yes      | Indicates if the preset has been archived |

Update a preset of an organization.

_Returned Response:_

[AddPresetResponse](#addpresetresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "presetName": "p1",
    "transformation": "t.flip()~t.flop()",
    "params": {
        "w": {
            "type": "integer",
            "default": 200
        },
        "h": {
            "type": "integer",
            "default": 400
        }
    },
    "archived": true
}
```

</details>

### deletePreset

**Summary**: Delete a preset.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.deletePreset(
        presetName="p1")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.deletePresetAsync(
        presetName="p1"))
    # use result
except Exception as e:
    print(e)

```

| Argument   | Type | Required | Description                      |
| ---------- | ---- | -------- | -------------------------------- |
| presetName | str  | yes      | Name of the preset to be deleted |

Delete a preset of an organization.

_Returned Response:_

[AddPresetResponse](#addpresetresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "presetName": "p1",
    "transformation": "t.flip()~t.flop()",
    "params": {
        "w": {
            "type": "integer",
            "default": 200
        },
        "h": {
            "type": "integer",
            "default": 400
        }
    },
    "archived": true
}
```

</details>

### getPreset

**Summary**: Get a preset.

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getPreset(
        presetName="p1")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getPresetAsync(
        presetName="p1"))
    # use result
except Exception as e:
    print(e)

```

| Argument   | Type | Required | Description                      |
| ---------- | ---- | -------- | -------------------------------- |
| presetName | str  | yes      | Name of the preset to be fetched |

Get a preset of an organization.

_Returned Response:_

[AddPresetResponse](#addpresetresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "presetName": "p1",
    "transformation": "t.flip()~t.flop()",
    "params": {
        "w": {
            "type": "integer",
            "default": 200
        },
        "h": {
            "type": "integer",
            "default": 400
        }
    },
    "archived": true
}
```

</details>

### getDefaultAssetForPlayground

**Summary**: Get default asset for playground

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getDefaultAssetForPlayground()
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getDefaultAssetForPlaygroundAsync())
    # use result
except Exception as e:
    print(e)

```

Get default asset for playground

_Returned Response:_

[UploadResponse](#uploadresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "_id": "dummy-uuid",
    "name": "asset",
    "path": "dir",
    "fileId": "dir/asset",
    "format": "jpeg",
    "size": 1000,
    "access": "private",
    "isActive": true,
    "tags": ["tag1", "tag2"],
    "metadata": {
        "key": "value"
    },
    "url": "https://domain.com/filename.jpeg"
}
```

</details>

### getModules

**Summary**: Get all transformation modules

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getModules()
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getModulesAsync())
    # use result
except Exception as e:
    print(e)

```

Get all transformation modules.

_Returned Response:_

[TransformationModulesResponse](#transformationmodulesresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "delimiters": {
        "operationSeparator": "~",
        "parameterSeparator": ":"
    },
    "plugins": {
        "erase": {
            "identifier": "erase",
            "name": "EraseBG",
            "description": "EraseBG Background Removal Module",
            "credentials": {
                "required": false
            },
            "operations": [
                {
                    "params": {
                        "name": "Industry Type",
                        "type": "enum",
                        "enum": ["general", "ecommerce"],
                        "default": "general",
                        "identifier": "i",
                        "title": "Industry type"
                    },
                    "displayName": "Remove background of an image",
                    "method": "bg",
                    "description": "Remove the background of any image"
                }
            ],
            "enabled": true
        }
    },
    "presets": [
        {
            "_id": "dummy-id",
            "createdAt": "2022-02-14T10:06:17.803Z",
            "updatedAt": "2022-02-14T10:06:17.803Z",
            "isActive": true,
            "orgId": "265",
            "presetName": "compressor",
            "transformation": "t.compress(q:95)",
            "archived": false
        }
    ]
}
```

</details>

### getModule

**Summary**: Get Transformation Module by module identifier

```python
import asyncio
from pixelbin import PixelbinClient, PixelbinConfig

config = PixelbinConfig({
    "domain": "https://api.pixelbin.io",
    "apiSecret": "API_SECRECT_TOKEN",
})

pixelbin:PixelbinClient = PixelbinClient(config=config)

# Sync method call
try:
    result = pixelbin.assets.getModule(
        identifier="t")
    # use result
except Exception as e:
    print(e)

# Async method call
try:
    result = asyncio.run(pixelbin.assets.getModuleAsync(
        identifier="t"))
    # use result
except Exception as e:
    print(e)

```

| Argument   | Type | Required | Description                         |
| ---------- | ---- | -------- | ----------------------------------- |
| identifier | str  | yes      | identifier of Transformation Module |

Get Transformation Module by module identifier

_Returned Response:_

[TransformationModuleResponse](#transformationmoduleresponse)

Success

<details>
<summary><i>&nbsp; Example:</i></summary>

```json
{
    "identifier": "erase",
    "name": "EraseBG",
    "description": "EraseBG Background Removal Module",
    "credentials": {
        "required": false
    },
    "operations": [
        {
            "params": {
                "name": "Industry Type",
                "type": "enum",
                "enum": ["general", "ecommerce"],
                "default": "general",
                "identifier": "i",
                "title": "Industry type"
            },
            "displayName": "Remove background of an image",
            "method": "bg",
            "description": "Remove the background of any image"
        }
    ],
    "enabled": true
}
```

</details>

### Schemas

#### folderItem

| Properties | Type | Nullable | Description                          |
| ---------- | ---- | -------- | ------------------------------------ |
| \_id       | str  | yes      | Id of the folder item                |
| name       | str  | yes      | Name of the folder item              |
| path       | str  | yes      | Path of containing folder            |
| type       | str  | yes      | Type of the item. `file` or `folder` |

#### exploreItem

| Properties | Type | Nullable | Description                                                     |
| ---------- | ---- | -------- | --------------------------------------------------------------- |
| \_id       | str  | yes      | id of the exploreItem                                           |
| name       | str  | yes      | name of the item                                                |
| type       | str  | yes      | Type of item whether `file` or `folder`                         |
| path       | str  | yes      | Path of containing folder                                       |
| fileId     | str  | no       | Combination of `path` and `name` of file                        |
| format     | str  | no       | Format of the file                                              |
| size       | int  | no       | Size of the file in bytes                                       |
| access     | str  | no       | Access level of asset, can be either `public-read` or `private` |

#### page

| Properties | Type | Nullable | Description                   |
| ---------- | ---- | -------- | ----------------------------- |
| type       | str  | yes      | Type of page                  |
| size       | int  | yes      | Number of items on the page   |
| current    | int  | yes      | Current page number.          |
| hasNext    | bool | yes      | Whether the next page exists. |
| itemTotal  | int  | yes      | Total number of items.        |

#### exploreResponse

| Properties | Type              | Nullable | Description                  |
| ---------- | ----------------- | -------- | ---------------------------- |
| items      | List[exploreItem] | yes      | exploreItems in current page |
| page       | page              | yes      | page details                 |

#### ListFilesResponse

| Properties | Type              | Nullable | Description                  |
| ---------- | ----------------- | -------- | ---------------------------- |
| items      | List[exploreItem] | yes      | exploreItems in current page |
| page       | page              | yes      | page details                 |

#### exploreFolderResponse

| Properties | Type              | Nullable | Description                  |
| ---------- | ----------------- | -------- | ---------------------------- |
| folder     | folderItem        | yes      | requested folder item        |
| items      | List[exploreItem] | yes      | exploreItems in current page |
| page       | page              | yes      | page details                 |

#### FileUploadRequest

| Properties       | Type       | Nullable | Description                                                                                                                                                                                                                      |
| ---------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| file             | FileIO     | yes      | Asset file                                                                                                                                                                                                                       |
| path             | str        | no       | Path where you want to store the asset. Path of containing folder                                                                                                                                                                |
| name             | str        | no       | Name of the asset, if not provided name of the file will be used. Note - The provided name will be slugified to make it URL safe                                                                                                 |
| access           | AccessEnum | no       | Access level of asset, can be either `public-read` or `private`                                                                                                                                                                  |
| tags             | List[str]  | no       | Asset tags                                                                                                                                                                                                                       |
| metadata         | Any        | no       | Asset related metadata                                                                                                                                                                                                           |
| overwrite        | bool       | no       | Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`.                                                                                                         |
| filenameOverride | bool       | no       | If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. |

#### UrlUploadRequest

| Properties       | Type       | Nullable | Description                                                                                                                                                                                                                      |
| ---------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| url              | str        | yes      | Asset URL                                                                                                                                                                                                                        |
| path             | str        | no       | Path where you want to store the asset. Path of containing folder.                                                                                                                                                               |
| name             | str        | no       | Name of the asset, if not provided name of the file will be used. Note - The provided name will be slugified to make it URL safe                                                                                                 |
| access           | AccessEnum | no       | Access level of asset, can be either `public-read` or `private`                                                                                                                                                                  |
| tags             | List[str]  | no       | Asset tags                                                                                                                                                                                                                       |
| metadata         | Any        | no       | Asset related metadata                                                                                                                                                                                                           |
| overwrite        | bool       | no       | Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`.                                                                                                         |
| filenameOverride | bool       | no       | If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. |

#### UploadResponse

| Properties | Type      | Nullable | Description                                                 |
| ---------- | --------- | -------- | ----------------------------------------------------------- |
| \_id       | str       | yes      | \_id of the item                                            |
| fileId     | str       | yes      | Combination of `path` and `name` of file                    |
| name       | str       | yes      | name of the item                                            |
| path       | str       | yes      | path to the parent folder                                   |
| format     | str       | yes      | format of the file                                          |
| size       | int       | yes      | size of file in bytes                                       |
| access     | str       | yes      | Access level of asset, can be either public-read or private |
| tags       | List[str] | no       | tags associated with the item                               |
| metadata   | Any       | no       | metadata associated with the item                           |
| url        | str       | no       | url of the item                                             |
| thumbnail  | str       | no       | url of item thumbnail                                       |

#### SignedUploadRequest

| Properties       | Type       | Nullable | Description                                                                                                                                                                                                                      |
| ---------------- | ---------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name             | str        | no       | name of the file                                                                                                                                                                                                                 |
| path             | str        | no       | Path of containing folder.                                                                                                                                                                                                       |
| format           | str        | no       | Format of the file                                                                                                                                                                                                               |
| access           | AccessEnum | no       | Access level of asset, can be either `public-read` or `private`                                                                                                                                                                  |
| tags             | List[str]  | no       | Tags associated with the file.                                                                                                                                                                                                   |
| metadata         | Any        | no       | Metadata associated with the file.                                                                                                                                                                                               |
| overwrite        | bool       | no       | Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`.                                                                                                         |
| filenameOverride | bool       | no       | If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. |

#### SignedUploadResponse

| Properties     | Type         | Nullable | Description                                  |
| -------------- | ------------ | -------- | -------------------------------------------- |
| s3PresignedUrl | PresignedUrl | yes      | `signedDetails` for upload with frontend sdk |
|  |

#### PresignedUrl

| Properties | Type | Nullable | Description                                 |
| ---------- | ---- | -------- | ------------------------------------------- |
| url        | str  | no       | `presigned url` for upload                  |
|  |
| fields     | Any  | no       | signed fields to be sent along with request |

#### FilesResponse

| Properties | Type      | Nullable | Description                                                    |
| ---------- | --------- | -------- | -------------------------------------------------------------- |
| \_id       | str       | yes      | \_id of the file                                               |
| name       | str       | yes      | name of the file                                               |
| path       | str       | yes      | path of containing folder.                                     |
| fileId     | str       | yes      | Combination of `path` and `name` of file                       |
| format     | str       | yes      | format of the file                                             |
| size       | int       | yes      | size of the file in bytes                                      |
| access     | str       | yes      | Access level of file, can be either `public-read` or `private` |
| isActive   | bool      | yes      | Whether the file is active                                     |
| tags       | List[str] | no       | Tags associated with the file                                  |
| metadata   | Any       | no       | Metadata associated with the file                              |
| url        | str       | no       | url of the file                                                |
| thumbnail  | str       | no       | url of the thumbnail of the file                               |

#### UpdateFileRequest

| Properties | Type      | Nullable | Description                                                     |
| ---------- | --------- | -------- | --------------------------------------------------------------- |
| name       | str       | no       | Name of the file                                                |
| path       | str       | no       | path of containing folder.                                      |
| access     | str       | no       | Access level of asset, can be either `public-read` or `private` |
| isActive   | bool      | no       | Whether the file is active                                      |
| tags       | List[str] | no       | Tags associated with the file                                   |
| metadata   | Any       | no       | Metadata associated with the file                               |

#### FoldersResponse

| Properties | Type | Nullable | Description                  |
| ---------- | ---- | -------- | ---------------------------- |
| \_id       | str  | yes      | \_id of the folder           |
| name       | str  | yes      | name of the folder           |
| path       | str  | yes      | path of containing folder.   |
| isActive   | bool | yes      | whether the folder is active |

#### CreateFolderRequest

| Properties | Type | Nullable | Description                |
| ---------- | ---- | -------- | -------------------------- |
| name       | str  | yes      | Name of the folder         |
| path       | str  | no       | path of containing folder. |

#### UpdateFolderRequest

| Properties | Type | Nullable | Description                  |
| ---------- | ---- | -------- | ---------------------------- |
| isActive   | bool | no       | whether the folder is active |

#### TransformationModulesResponse

| Properties | Type      | Nullable | Description                                         |
| ---------- | --------- | -------- | --------------------------------------------------- |
| delimiters | Delimiter | no       | Delimiter for parsing plugin schema                 |
| plugins    | Any       | no       | Transformations currently supported by the pixelbin |
| presets    | List[Any] | no       | List of saved presets                               |

#### DeleteMultipleFilesRequest

| Properties | Type      | Nullable | Description                   |
| ---------- | --------- | -------- | ----------------------------- |
| ids        | List[str] | yes      | Array of file \_ids to delete |

#### Delimiter

| Properties         | Type | Nullable | Description                                                              |
| ------------------ | ---- | -------- | ------------------------------------------------------------------------ |
| operationSeparator | str  | no       | separator to separate operations in the url pattern                      |
| parameterSeparator | str  | no       | separator to separate parameters used with operations in the url pattern |

#### TransformationModuleResponse

| Properties  | Type      | Nullable | Description                                     |
| ----------- | --------- | -------- | ----------------------------------------------- |
| identifier  | str       | no       | identifier for the plugin type                  |
| name        | str       | no       | name of the plugin                              |
| description | str       | no       | description of the plugin                       |
| credentials | Any       | no       | credentials, if any, associated with the plugin |
| operations  | List[Any] | no       | supported operations in the plugin              |
| enabled     | bool      | no       | whether the plugin is enabled                   |

#### Credentials

| Properties  | Type | Nullable | Description                                                 |
| ----------- | ---- | -------- | ----------------------------------------------------------- |
| \_id        | str  | no       | Unique ID for credential                                    |
| createdAt   | str  | no       | Credential creation ISO timestamp                           |
| updatedAt   | str  | no       | Credential update ISO timestamp                             |
| isActive    | bool | no       | Tells if credential is active or not                        |
| orgId       | str  | no       | ID of the organization this credential belongs to           |
| pluginId    | str  | no       | Unique identifier for the plugin this credential belongs to |
| credentials | Any  | no       | Credentials object. It is different for each plugin         |
| description | Any  | no       |                                                             |

#### CredentialsItem

| Properties | Type | Nullable | Description |
| ---------- | ---- | -------- | ----------- |
| pluginId   | Any  | no       |             |

#### AddCredentialsRequest

| Properties  | Type | Nullable | Description                                                 |
| ----------- | ---- | -------- | ----------------------------------------------------------- |
| credentials | Any  | yes      | Credentials of the plugin                                   |
| pluginId    | str  | yes      | Unique identifier for the plugin this credential belongs to |

#### UpdateCredentialsRequest

| Properties  | Type | Nullable | Description               |
| ----------- | ---- | -------- | ------------------------- |
| credentials | Any  | yes      | Credentials of the plugin |

#### AddCredentialsResponse

| Properties  | Type | Nullable | Description |
| ----------- | ---- | -------- | ----------- |
| credentials | Any  | no       |             |

#### DeleteCredentialsResponse

| Properties  | Type | Nullable | Description                                                 |
| ----------- | ---- | -------- | ----------------------------------------------------------- |
| \_id        | str  | no       | Unique Credential ID                                        |
| createdAt   | str  | no       | Credential creation ISO timestamp                           |
| updatedAt   | str  | no       | Credential update ISO timestamp                             |
| isActive    | bool | no       | Tells if credential is active or not                        |
| orgId       | str  | no       | ID of the organization this credential belongs to           |
| pluginId    | str  | no       | Unique identifier for the plugin this credential belongs to |
| credentials | Any  | no       | Credentials object. It is different for each plugin         |

#### GetAncestorsResponse

| Properties | Type                  | Nullable | Description |
| ---------- | --------------------- | -------- | ----------- |
| folder     | folderItem            | no       |             |
| ancestors  | List[FoldersResponse] | no       |             |

#### GetFilesWithConstraintsItem

| Properties | Type | Nullable | Description |
| ---------- | ---- | -------- | ----------- |
| path       | str  | no       |             |
| name       | str  | no       |             |
| type       | str  | no       |             |

#### GetFilesWithConstraintsRequest

| Properties | Type                              | Nullable | Description |
| ---------- | --------------------------------- | -------- | ----------- |
| items      | List[GetFilesWithConstraintsItem] | no       |             |
| maxCount   | float                             | no       |             |
| maxSize    | float                             | no       |             |

#### AddPresetRequest

| Properties     | Type | Nullable | Description                                    |
| -------------- | ---- | -------- | ---------------------------------------------- |
| presetName     | str  | yes      | Name of the preset                             |
| transformation | str  | yes      | A chain of transformations, separated by `~`   |
| params         | Any  | no       | Parameters object for transformation variables |

#### AddPresetResponse

| Properties     | Type | Nullable | Description                                    |
| -------------- | ---- | -------- | ---------------------------------------------- |
| presetName     | str  | yes      | Name of the preset                             |
| transformation | str  | yes      | A chain of transformations, separated by `~`   |
| params         | Any  | no       | Parameters object for transformation variables |
| archived       | bool | no       | Indicates if the preset has been archived      |

#### UpdatePresetRequest

| Properties | Type | Nullable | Description                               |
| ---------- | ---- | -------- | ----------------------------------------- |
| archived   | bool | yes      | Indicates if the preset has been archived |

#### GetPresetsResponse

| Properties | Type                    | Nullable | Description             |
| ---------- | ----------------------- | -------- | ----------------------- |
| items      | List[AddPresetResponse] | yes      | Presets in current page |
| page       | page                    | yes      | page details            |

### Enums

#### [AccessEnum](#AccessEnum)

Type : string

| Name        | Value       | Description |
| ----------- | ----------- | ----------- |
| public-read | public-read | public-read |
| private     | private     | private     |

---
