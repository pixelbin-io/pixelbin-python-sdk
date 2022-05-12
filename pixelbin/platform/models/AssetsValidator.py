"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class AssetsValidator:
    
    class fileUpload(BaseSchema):
        
        pass 
    
    class urlUpload(BaseSchema):
        
        pass 
    
    class createSignedUrl(BaseSchema):
        
        pass 
    
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
    
    class updateFolder(BaseSchema):
        
        folderId = fields.Str(required=False)
         
    
    class deleteFolder(BaseSchema):
        
        _id = fields.Str(required=False)
         
    
    class getModules(BaseSchema):
        
        pass 
    
    class getModule(BaseSchema):
        
        identifier = fields.Str(required=False)
         
    