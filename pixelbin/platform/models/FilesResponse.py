"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class FilesResponse(BaseSchema):
    # Assets swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    fileId = fields.Str(required=False)
    
    format = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    access = fields.Str(required=False)
    
    isActive = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    metadata = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    thumbnail = fields.Str(required=False)
    

