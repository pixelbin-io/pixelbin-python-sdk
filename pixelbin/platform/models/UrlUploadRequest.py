"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class UrlUploadRequest(BaseSchema):
    # Assets swagger.json

    
    url = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    access = fields.Str(required=False, validate=OneOf([val.value for val in AccessEnum.__members__.values()]))
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    metadata = fields.Dict(required=False)
    
    overwrite = fields.Boolean(required=False)
    
    filenameOverride = fields.Boolean(required=False)
    

