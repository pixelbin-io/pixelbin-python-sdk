
import asyncio
import ujson
from ..common.aiohttp_helper import AiohttpHelper
from ..common.exceptions import PixelbinServerResponseError
from .PlatformAPIClient import APIClient
from .PixelbinConfig import PixelbinConfig
from io import FileIO
from typing import List, Any



from .enums import AccessEnum




from .models.AssetsValidator import AssetsValidator
from .models.OrganizationValidator import OrganizationValidator


class PixelbinClient:
    """PixelbinClient is wrapper class for hitting pixelbin apis"""

    def __init__(self, config: PixelbinConfig):
        """
        summary: create instance of PixelbinClient
        
        :param - config : instances of PixelbinConfig : Type - PixelbinConfig
        """
        self.config = config
        self.assets = Assets(config)
        self.organization = Organization(config)
        
    



class Assets:
    def __init__(self, config):
        self.config = config
    
    
    
    

       
    async def fileUploadAsync(
        self, 
        
        file:FileIO=None, 
        path:str=None, 
        name:str=None, 
        access:AccessEnum=None, 
        tags:List[str]=None, 
        metadata:Any=None, 
        overwrite:bool=None, 
        filenameOverride:bool=None
        ) -> dict:   
        """
        summary: Upload File
        description: Upload File to Pixelbin
        
        :param - file : Asset file : Type - FileIO
        :param - path : Path where you want to store the asset. Path of containing folder : Type - str
        :param - name : Name of the asset, if not provided name of the file will be used. Note - The provided name will be slugified to make it URL safe : Type - str
        :param - access : Access level of asset, can be either `public-read` or `private` : Type - AccessEnum
        :param - tags : Asset tags : Type - List[str]
        :param - metadata : Asset related metadata : Type - Any
        :param - overwrite : Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`. : Type - bool
        :param - filenameOverride : If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. : Type - bool
        """

        payload = {}
        

        # Parameter validation
        schema = AssetsValidator.fileUpload()
        schema.dump(schema.load(payload))

        
        body = {}
        
        if file is not None:
            body["file"] = file
        
        if path is not None:
            body["path"] = path
        
        if name is not None:
            body["name"] = name
        
        if access is not None:
            body["access"] = access
        
        if tags is not None:
            body["tags"] = tags
        
        if metadata is not None:
            body["metadata"] = metadata
        
        if overwrite is not None:
            body["overwrite"] = overwrite
        
        if filenameOverride is not None:
            body["filenameOverride"] = filenameOverride
        
        # Body validation
        from .models.FileUploadRequest import FileUploadRequest
        schema = FileUploadRequest()
        schema.dump(schema.load(body))
        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="post",
            url=f"/service/platform/assets/v1.0/upload/direct",
            query=query_params,
            body=body,
            contentType="multipart/form-data"
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def fileUpload(
        self, 
        
        file:FileIO=None, 
        path:str=None, 
        name:str=None, 
        access:AccessEnum=None, 
        tags:List[str]=None, 
        metadata:Any=None, 
        overwrite:bool=None, 
        filenameOverride:bool=None
        ):   
        """
        summary: Upload File
        description: Upload File to Pixelbin
        
        :param - file : Asset file : Type - FileIO
        :param - path : Path where you want to store the asset. Path of containing folder : Type - str
        :param - name : Name of the asset, if not provided name of the file will be used. Note - The provided name will be slugified to make it URL safe : Type - str
        :param - access : Access level of asset, can be either `public-read` or `private` : Type - AccessEnum
        :param - tags : Asset tags : Type - List[str]
        :param - metadata : Asset related metadata : Type - Any
        :param - overwrite : Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`. : Type - bool
        :param - filenameOverride : If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. : Type - bool
        """
        return asyncio.get_event_loop().run_until_complete(
            self.fileUploadAsync(
                file=file, 
                path=path, 
                name=name, 
                access=access, 
                tags=tags, 
                metadata=metadata, 
                overwrite=overwrite, 
                filenameOverride=filenameOverride)
        )

    
    
    

        
    async def urlUploadAsync(
        self, 
        
        url:str=None, 
        path:str=None, 
        name:str=None, 
        access:AccessEnum=None, 
        tags:List[str]=None, 
        metadata:Any=None, 
        overwrite:bool=None, 
        filenameOverride:bool=None
        ) -> dict:   
        """
        summary: Upload Asset with url
        description: Upload Asset with url
        
        :param - url : Asset URL : Type - str
        :param - path : Path where you want to store the asset. Path of containing folder. : Type - str
        :param - name : Name of the asset, if not provided name of the file will be used. Note - The provided name will be slugified to make it URL safe : Type - str
        :param - access : Access level of asset, can be either `public-read` or `private` : Type - AccessEnum
        :param - tags : Asset tags : Type - List[str]
        :param - metadata : Asset related metadata : Type - Any
        :param - overwrite : Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`. : Type - bool
        :param - filenameOverride : If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. : Type - bool
        """

        payload = {}
        

        # Parameter validation
        schema = AssetsValidator.urlUpload()
        schema.dump(schema.load(payload))

        
        body = {}
        
        if url is not None:
            body["url"] = url
        
        if path is not None:
            body["path"] = path
        
        if name is not None:
            body["name"] = name
        
        if access is not None:
            body["access"] = access
        
        if tags is not None:
            body["tags"] = tags
        
        if metadata is not None:
            body["metadata"] = metadata
        
        if overwrite is not None:
            body["overwrite"] = overwrite
        
        if filenameOverride is not None:
            body["filenameOverride"] = filenameOverride
        
        # Body validation
        from .models.UrlUploadRequest import UrlUploadRequest
        schema = UrlUploadRequest()
        schema.dump(schema.load(body))
        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="post",
            url=f"/service/platform/assets/v1.0/upload/url",
            query=query_params,
            body=body,
            contentType="application/json"
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def urlUpload(
        self, 
        
        url:str=None, 
        path:str=None, 
        name:str=None, 
        access:AccessEnum=None, 
        tags:List[str]=None, 
        metadata:Any=None, 
        overwrite:bool=None, 
        filenameOverride:bool=None
        ):   
        """
        summary: Upload Asset with url
        description: Upload Asset with url
        
        :param - url : Asset URL : Type - str
        :param - path : Path where you want to store the asset. Path of containing folder. : Type - str
        :param - name : Name of the asset, if not provided name of the file will be used. Note - The provided name will be slugified to make it URL safe : Type - str
        :param - access : Access level of asset, can be either `public-read` or `private` : Type - AccessEnum
        :param - tags : Asset tags : Type - List[str]
        :param - metadata : Asset related metadata : Type - Any
        :param - overwrite : Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`. : Type - bool
        :param - filenameOverride : If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. : Type - bool
        """
        return asyncio.get_event_loop().run_until_complete(
            self.urlUploadAsync(
                url=url, 
                path=path, 
                name=name, 
                access=access, 
                tags=tags, 
                metadata=metadata, 
                overwrite=overwrite, 
                filenameOverride=filenameOverride)
        )

    
    
    

        
    async def createSignedUrlAsync(
        self, 
        
        name:str=None, 
        path:str=None, 
        format:str=None, 
        access:AccessEnum=None, 
        tags:List[str]=None, 
        metadata:Any=None, 
        overwrite:bool=None, 
        filenameOverride:bool=None
        ) -> dict:   
        """
        summary: S3 Signed URL upload
        description: For the given asset details, a S3 signed URL will be generated,
which can be then used to upload your asset.

        
        :param - name : name of the file : Type - str
        :param - path : Path of containing folder. : Type - str
        :param - format : Format of the file : Type - str
        :param - access : Access level of asset, can be either `public-read` or `private` : Type - AccessEnum
        :param - tags : Tags associated with the file. : Type - List[str]
        :param - metadata : Metadata associated with the file. : Type - Any
        :param - overwrite : Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`. : Type - bool
        :param - filenameOverride : If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. : Type - bool
        """

        payload = {}
        

        # Parameter validation
        schema = AssetsValidator.createSignedUrl()
        schema.dump(schema.load(payload))

        
        body = {}
        
        if name is not None:
            body["name"] = name
        
        if path is not None:
            body["path"] = path
        
        if format is not None:
            body["format"] = format
        
        if access is not None:
            body["access"] = access
        
        if tags is not None:
            body["tags"] = tags
        
        if metadata is not None:
            body["metadata"] = metadata
        
        if overwrite is not None:
            body["overwrite"] = overwrite
        
        if filenameOverride is not None:
            body["filenameOverride"] = filenameOverride
        
        # Body validation
        from .models.SignedUploadRequest import SignedUploadRequest
        schema = SignedUploadRequest()
        schema.dump(schema.load(body))
        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="post",
            url=f"/service/platform/assets/v1.0/upload/signed-url",
            query=query_params,
            body=body,
            contentType="application/json"
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def createSignedUrl(
        self, 
        
        name:str=None, 
        path:str=None, 
        format:str=None, 
        access:AccessEnum=None, 
        tags:List[str]=None, 
        metadata:Any=None, 
        overwrite:bool=None, 
        filenameOverride:bool=None
        ):   
        """
        summary: S3 Signed URL upload
        description: For the given asset details, a S3 signed URL will be generated,
which can be then used to upload your asset.

        
        :param - name : name of the file : Type - str
        :param - path : Path of containing folder. : Type - str
        :param - format : Format of the file : Type - str
        :param - access : Access level of asset, can be either `public-read` or `private` : Type - AccessEnum
        :param - tags : Tags associated with the file. : Type - List[str]
        :param - metadata : Metadata associated with the file. : Type - Any
        :param - overwrite : Overwrite flag. If set to `true` will overwrite any file that exists with same path, name and type. Defaults to `false`. : Type - bool
        :param - filenameOverride : If set to `true` will add unique characters to name if asset with given name already exists. If overwrite flag is set to `true`, preference will be given to overwrite flag. If both are set to `false` an error will be raised. : Type - bool
        """
        return asyncio.get_event_loop().run_until_complete(
            self.createSignedUrlAsync(
                name=name, 
                path=path, 
                format=format, 
                access=access, 
                tags=tags, 
                metadata=metadata, 
                overwrite=overwrite, 
                filenameOverride=filenameOverride)
        )

    
    
    

    
    async def listFilesAsync(
        self, 
        
        name:str=None, 
        path:str=None, 
        format:str=None, 
        tags:List[Any]=None, 
        onlyFiles:bool=None, 
        onlyFolders:bool=None, 
        pageNo:int=None, 
        pageSize:int=None, 
        sort:str=None
        ) -> dict:   
        """
        summary: List and search files and folders.
        description: List all files and folders in root folder. Search for files if name is provided. If path is provided, search in the specified path.

        :param - name : Find items with matching name: Type - str 
        :param - path : Find items with matching path: Type - str 
        :param - format : Find items with matching format: Type - str 
        :param - tags : Find items containing these tags: Type - List[str] 
        :param - onlyFiles : If true will fetch only files: Type - bool 
        :param - onlyFolders : If true will fetch only folders: Type - bool 
        :param - pageNo : Page No.: Type - int 
        :param - pageSize : Page Size: Type - int 
        :param - sort : Key to sort results by. A "-" suffix will sort results in descending orders.
: Type - str 
        
        """

        payload = {}
        
        if name is not None:
            payload["name"] = name
        
        if path is not None:
            payload["path"] = path
        
        if format is not None:
            payload["format"] = format
        
        if tags is not None:
            payload["tags"] = tags
        
        if onlyFiles is not None:
            payload["onlyFiles"] = onlyFiles
        
        if onlyFolders is not None:
            payload["onlyFolders"] = onlyFolders
        
        if pageNo is not None:
            payload["pageNo"] = pageNo
        
        if pageSize is not None:
            payload["pageSize"] = pageSize
        
        if sort is not None:
            payload["sort"] = sort
        

        # Parameter validation
        schema = AssetsValidator.listFiles()
        schema.dump(schema.load(payload))

        

        query_params = {}
        
        if name:
            query_params['name'] = name
        
        if path:
            query_params['path'] = path
        
        if format:
            query_params['format'] = format
        
        if tags:
            query_params['tags'] = tags
        
        if onlyFiles:
            query_params['onlyFiles'] = onlyFiles
        
        if onlyFolders:
            query_params['onlyFolders'] = onlyFolders
        
        if pageNo:
            query_params['pageNo'] = pageNo
        
        if pageSize:
            query_params['pageSize'] = pageSize
        
        if sort:
            query_params['sort'] = sort
        

        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=f"/service/platform/assets/v1.0/listFiles",
            query=query_params,
            body=None,
            contentType=""
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def listFiles(
        self, 
        
        name:str=None, 
        path:str=None, 
        format:str=None, 
        tags:List[Any]=None, 
        onlyFiles:bool=None, 
        onlyFolders:bool=None, 
        pageNo:int=None, 
        pageSize:int=None, 
        sort:str=None
        ):   
        """
        summary: List and search files and folders.
        description: List all files and folders in root folder. Search for files if name is provided. If path is provided, search in the specified path.

        :param - name : Find items with matching name: Type - str 
        :param - path : Find items with matching path: Type - str 
        :param - format : Find items with matching format: Type - str 
        :param - tags : Find items containing these tags: Type - List[str] 
        :param - onlyFiles : If true will fetch only files: Type - bool 
        :param - onlyFolders : If true will fetch only folders: Type - bool 
        :param - pageNo : Page No.: Type - int 
        :param - pageSize : Page Size: Type - int 
        :param - sort : Key to sort results by. A "-" suffix will sort results in descending orders.
: Type - str 
        
        """
        return asyncio.get_event_loop().run_until_complete(
            self.listFilesAsync(
                name=name, 
                path=path, 
                format=format, 
                tags=tags, 
                onlyFiles=onlyFiles, 
                onlyFolders=onlyFolders, 
                pageNo=pageNo, 
                pageSize=pageSize, 
                sort=sort)
        )

    
    
    

    
    async def getFileByIdAsync(
        self, 
        
        _id:str=None
        ) -> dict:   
        """
        summary: Get file details with _id
        description: 
        :param - _id : _id of File: Type - str 
        
        """

        payload = {}
        
        if _id is not None:
            payload["_id"] = _id
        

        # Parameter validation
        schema = AssetsValidator.getFileById()
        schema.dump(schema.load(payload))

        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=f"/service/platform/assets/v1.0/files/id/{_id}",
            query=query_params,
            body=None,
            contentType=""
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def getFileById(
        self, 
        
        _id:str=None
        ):   
        """
        summary: Get file details with _id
        description: 
        :param - _id : _id of File: Type - str 
        
        """
        return asyncio.get_event_loop().run_until_complete(
            self.getFileByIdAsync(
                _id=_id)
        )

    
    
    

    
    async def getFileByFileIdAsync(
        self, 
        
        fileId:str=None
        ) -> dict:   
        """
        summary: Get file details with fileId
        description: 
        :param - fileId : Combination of `path` and `name` of file: Type - str 
        
        """

        payload = {}
        
        if fileId is not None:
            payload["fileId"] = fileId
        

        # Parameter validation
        schema = AssetsValidator.getFileByFileId()
        schema.dump(schema.load(payload))

        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=f"/service/platform/assets/v1.0/files/{fileId}",
            query=query_params,
            body=None,
            contentType=""
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def getFileByFileId(
        self, 
        
        fileId:str=None
        ):   
        """
        summary: Get file details with fileId
        description: 
        :param - fileId : Combination of `path` and `name` of file: Type - str 
        
        """
        return asyncio.get_event_loop().run_until_complete(
            self.getFileByFileIdAsync(
                fileId=fileId)
        )

    
    
    

        
    async def updateFileAsync(
        self, 
        
        fileId:str=None,
        name:str=None, 
        path:str=None, 
        access:str=None, 
        isActive:bool=None, 
        tags:List[str]=None, 
        metadata:Any=None
        ) -> dict:   
        """
        summary: Update file details
        description: 
        :param - fileId : Combination of `path` and `name`: Type - str 
        
        :param - name : Name of the file : Type - str
        :param - path : path of containing folder. : Type - str
        :param - access : Access level of asset, can be either `public-read` or `private` : Type - str
        :param - isActive : Whether the file is active : Type - bool
        :param - tags : Tags associated with the file : Type - List[str]
        :param - metadata : Metadata associated with the file : Type - Any
        """

        payload = {}
        
        if fileId is not None:
            payload["fileId"] = fileId
        

        # Parameter validation
        schema = AssetsValidator.updateFile()
        schema.dump(schema.load(payload))

        
        body = {}
        
        if name is not None:
            body["name"] = name
        
        if path is not None:
            body["path"] = path
        
        if access is not None:
            body["access"] = access
        
        if isActive is not None:
            body["isActive"] = isActive
        
        if tags is not None:
            body["tags"] = tags
        
        if metadata is not None:
            body["metadata"] = metadata
        
        # Body validation
        from .models.UpdateFileRequest import UpdateFileRequest
        schema = UpdateFileRequest()
        schema.dump(schema.load(body))
        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="patch",
            url=f"/service/platform/assets/v1.0/files/{fileId}",
            query=query_params,
            body=body,
            contentType="application/json"
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def updateFile(
        self, 
        
        fileId:str=None,
        name:str=None, 
        path:str=None, 
        access:str=None, 
        isActive:bool=None, 
        tags:List[str]=None, 
        metadata:Any=None
        ):   
        """
        summary: Update file details
        description: 
        :param - fileId : Combination of `path` and `name`: Type - str 
        
        :param - name : Name of the file : Type - str
        :param - path : path of containing folder. : Type - str
        :param - access : Access level of asset, can be either `public-read` or `private` : Type - str
        :param - isActive : Whether the file is active : Type - bool
        :param - tags : Tags associated with the file : Type - List[str]
        :param - metadata : Metadata associated with the file : Type - Any
        """
        return asyncio.get_event_loop().run_until_complete(
            self.updateFileAsync(
                fileId=fileId,
                name=name, 
                path=path, 
                access=access, 
                isActive=isActive, 
                tags=tags, 
                metadata=metadata)
        )

    
    
    

    
    async def deleteFileAsync(
        self, 
        
        fileId:str=None
        ) -> dict:   
        """
        summary: Delete file
        description: 
        :param - fileId : Combination of `path` and `name`: Type - str 
        
        """

        payload = {}
        
        if fileId is not None:
            payload["fileId"] = fileId
        

        # Parameter validation
        schema = AssetsValidator.deleteFile()
        schema.dump(schema.load(payload))

        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="delete",
            url=f"/service/platform/assets/v1.0/files/{fileId}",
            query=query_params,
            body=None,
            contentType=""
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def deleteFile(
        self, 
        
        fileId:str=None
        ):   
        """
        summary: Delete file
        description: 
        :param - fileId : Combination of `path` and `name`: Type - str 
        
        """
        return asyncio.get_event_loop().run_until_complete(
            self.deleteFileAsync(
                fileId=fileId)
        )

    
    
    

        
    async def deleteFilesAsync(
        self, 
        
        ids:List[str]=None
        ) -> dict:   
        """
        summary: Delete multiple files
        description: 
        
        :param - ids : Array of file _ids to delete : Type - List[str]
        """

        payload = {}
        

        # Parameter validation
        schema = AssetsValidator.deleteFiles()
        schema.dump(schema.load(payload))

        
        body = {}
        
        if ids is not None:
            body["ids"] = ids
        
        # Body validation
        from .models.DeleteMultipleFilesRequest import DeleteMultipleFilesRequest
        schema = DeleteMultipleFilesRequest()
        schema.dump(schema.load(body))
        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="post",
            url=f"/service/platform/assets/v1.0/files/delete",
            query=query_params,
            body=body,
            contentType="application/json"
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def deleteFiles(
        self, 
        
        ids:List[str]=None
        ):   
        """
        summary: Delete multiple files
        description: 
        
        :param - ids : Array of file _ids to delete : Type - List[str]
        """
        return asyncio.get_event_loop().run_until_complete(
            self.deleteFilesAsync(
                ids=ids)
        )

    
    
    

        
    async def createFolderAsync(
        self, 
        
        name:str=None, 
        path:str=None
        ) -> dict:   
        """
        summary: Create folder
        description: Create a new folder at the specified path. Also creates the ancestors if they do not exist.

        
        :param - name : Name of the folder : Type - str
        :param - path : path of containing folder. : Type - str
        """

        payload = {}
        

        # Parameter validation
        schema = AssetsValidator.createFolder()
        schema.dump(schema.load(payload))

        
        body = {}
        
        if name is not None:
            body["name"] = name
        
        if path is not None:
            body["path"] = path
        
        # Body validation
        from .models.CreateFolderRequest import CreateFolderRequest
        schema = CreateFolderRequest()
        schema.dump(schema.load(body))
        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="post",
            url=f"/service/platform/assets/v1.0/folders",
            query=query_params,
            body=body,
            contentType="application/json"
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def createFolder(
        self, 
        
        name:str=None, 
        path:str=None
        ):   
        """
        summary: Create folder
        description: Create a new folder at the specified path. Also creates the ancestors if they do not exist.

        
        :param - name : Name of the folder : Type - str
        :param - path : path of containing folder. : Type - str
        """
        return asyncio.get_event_loop().run_until_complete(
            self.createFolderAsync(
                name=name, 
                path=path)
        )

    
    
    

        
    async def updateFolderAsync(
        self, 
        
        folderId:str=None,
        isActive:bool=None
        ) -> dict:   
        """
        summary: Update folder details
        description: Update folder details. Eg: Soft delete it
by making `isActive` as `false`.
We currently do not support updating folder name or path.

        :param - folderId : combination of `path` and `name`: Type - str 
        
        :param - isActive : whether the folder is active : Type - bool
        """

        payload = {}
        
        if folderId is not None:
            payload["folderId"] = folderId
        

        # Parameter validation
        schema = AssetsValidator.updateFolder()
        schema.dump(schema.load(payload))

        
        body = {}
        
        if isActive is not None:
            body["isActive"] = isActive
        
        # Body validation
        from .models.UpdateFolderRequest import UpdateFolderRequest
        schema = UpdateFolderRequest()
        schema.dump(schema.load(body))
        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="patch",
            url=f"/service/platform/assets/v1.0/folders/{folderId}",
            query=query_params,
            body=body,
            contentType="application/json"
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def updateFolder(
        self, 
        
        folderId:str=None,
        isActive:bool=None
        ):   
        """
        summary: Update folder details
        description: Update folder details. Eg: Soft delete it
by making `isActive` as `false`.
We currently do not support updating folder name or path.

        :param - folderId : combination of `path` and `name`: Type - str 
        
        :param - isActive : whether the folder is active : Type - bool
        """
        return asyncio.get_event_loop().run_until_complete(
            self.updateFolderAsync(
                folderId=folderId,
                isActive=isActive)
        )

    
    
    

    
    async def deleteFolderAsync(
        self, 
        
        _id:str=None
        ) -> dict:   
        """
        summary: Delete folder
        description: Delete folder and all its children permanently.

        :param - _id : _id of folder to be deleted: Type - str 
        
        """

        payload = {}
        
        if _id is not None:
            payload["_id"] = _id
        

        # Parameter validation
        schema = AssetsValidator.deleteFolder()
        schema.dump(schema.load(payload))

        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="delete",
            url=f"/service/platform/assets/v1.0/folders/{_id}",
            query=query_params,
            body=None,
            contentType=""
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def deleteFolder(
        self, 
        
        _id:str=None
        ):   
        """
        summary: Delete folder
        description: Delete folder and all its children permanently.

        :param - _id : _id of folder to be deleted: Type - str 
        
        """
        return asyncio.get_event_loop().run_until_complete(
            self.deleteFolderAsync(
                _id=_id)
        )

    
    
    

    
    async def getModulesAsync(
        self, 
        
        ) -> dict:   
        """
        summary: Get all transformation modules
        description: Get all transformation modules.

        
        """

        payload = {}
        

        # Parameter validation
        schema = AssetsValidator.getModules()
        schema.dump(schema.load(payload))

        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=f"/service/platform/assets/v1.0/playground/plugins",
            query=query_params,
            body=None,
            contentType=""
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def getModules(
        self, 
        
        ):   
        """
        summary: Get all transformation modules
        description: Get all transformation modules.

        
        """
        return asyncio.get_event_loop().run_until_complete(
            self.getModulesAsync()
        )

    
    
    

    
    async def getModuleAsync(
        self, 
        
        identifier:str=None
        ) -> dict:   
        """
        summary: Get Transformation Module by module identifier
        description: Get Transformation Module by module identifier

        :param - identifier : identifier of Transformation Module: Type - str 
        
        """

        payload = {}
        
        if identifier is not None:
            payload["identifier"] = identifier
        

        # Parameter validation
        schema = AssetsValidator.getModule()
        schema.dump(schema.load(payload))

        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=f"/service/platform/assets/v1.0/playground/plugins/{identifier}",
            query=query_params,
            body=None,
            contentType=""
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def getModule(
        self, 
        
        identifier:str=None
        ):   
        """
        summary: Get Transformation Module by module identifier
        description: Get Transformation Module by module identifier

        :param - identifier : identifier of Transformation Module: Type - str 
        
        """
        return asyncio.get_event_loop().run_until_complete(
            self.getModuleAsync(
                identifier=identifier)
        )

    
    



class Organization:
    def __init__(self, config):
        self.config = config
    
    
    
    

    
    async def getAppByTokenAsync(
        self, 
        
        token:str=None
        ) -> dict:   
        """
        summary: Get App Details
        description: Get App and org details with the API_TOKEN
        :param - token : Pixelbin api token: Type - str 
        
        """

        payload = {}
        
        if token is not None:
            payload["token"] = token
        

        # Parameter validation
        schema = OrganizationValidator.getAppByToken()
        schema.dump(schema.load(payload))

        

        query_params = {}
        

        response = await APIClient.execute(
            conf=self.config,
            method="get",
            url=f"/service/platform/organization/v1.0/apps/{token}",
            query=query_params,
            body=None,
            contentType=""
            )
        if response["status_code"] != 200:
            raise PixelbinServerResponseError(str(response["content"]))
        return ujson.loads(response["content"])

    def getAppByToken(
        self, 
        
        token:str=None
        ):   
        """
        summary: Get App Details
        description: Get App and org details with the API_TOKEN
        :param - token : Pixelbin api token: Type - str 
        
        """
        return asyncio.get_event_loop().run_until_complete(
            self.getAppByTokenAsync(
                token=token)
        )

    
    

