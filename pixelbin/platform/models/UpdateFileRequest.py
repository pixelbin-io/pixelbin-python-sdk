"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class UpdateFileRequest(BaseSchema):
    # Assets swagger.json

    
    name = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    access = fields.Str(required=False, validate=OneOf([val.value for val in AccessEnum.__members__.values()]))
    
    isActive = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    metadata = fields.Dict(required=False)
    

