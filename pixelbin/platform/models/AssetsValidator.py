"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class AssetsValidator:
    
    class addCredentials(BaseSchema):
        
        pass 
    
    class updateCredentials(BaseSchema):
        
        pluginId = fields.Str(required=False)
         
    
    class deleteCredentials(BaseSchema):
        
        pluginId = fields.Str(required=False)
         
    
    class getFileById(BaseSchema):
        
        _id = fields.Str(required=False)
         
    
    class getFileByFileId(BaseSchema):
        
        fileId = fields.Str(required=False)
         
    
    class updateFile(BaseSchema):
        
        fileId = fields.Str(required=False)
         
    
    class deleteFile(BaseSchema):
        
        fileId = fields.Str(required=False)
         
    
    class deleteFiles(BaseSchema):
        
        pass 
    
    class createFolder(BaseSchema):
        
        pass 
    
    class getFolderDetails(BaseSchema):
        
        path = fields.Str(required=False)
        
        name = fields.Str(required=False)
         
    
    class updateFolder(BaseSchema):
        
        folderId = fields.Str(required=False)
         
    
    class deleteFolder(BaseSchema):
        
        _id = fields.Str(required=False)
         
    
    class getFolderAncestors(BaseSchema):
        
        _id = fields.Str(required=False)
         
    
    class listFiles(BaseSchema):
        
        name = fields.Str(required=False)
        
        path = fields.Str(required=False)
        
        format = fields.Str(required=False)
        
        tags = fields.List(fields.Str(required=False), required=False)
        
        onlyFiles = fields.Boolean(required=False)
        
        onlyFolders = fields.Boolean(required=False)
        
        pageNo = fields.Int(required=False)
        
        pageSize = fields.Int(required=False)
        
        sort = fields.Str(required=False)
         
    
    class getDefaultAssetForPlayground(BaseSchema):
        
        pass 
    
    class getModules(BaseSchema):
        
        pass 
    
    class getModule(BaseSchema):
        
        identifier = fields.Str(required=False)
         
    
    class addPreset(BaseSchema):
        
        pass 
    
    class getPresets(BaseSchema):
        
        pass 
    
    class updatePreset(BaseSchema):
        
        presetName = fields.Str(required=False)
         
    
    class deletePreset(BaseSchema):
        
        presetName = fields.Str(required=False)
         
    
    class getPreset(BaseSchema):
        
        presetName = fields.Str(required=False)
         
    
    class fileUpload(BaseSchema):
        
        pass 
    
    class urlUpload(BaseSchema):
        
        pass 
    
    class createSignedUrl(BaseSchema):
        
        pass 
    
    class createSignedUrlV2(BaseSchema):
        
        pass 
    