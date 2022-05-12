"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class TransformationModuleResponse(BaseSchema):
    # Assets swagger.json

    
    identifier = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    credentials = fields.Dict(required=False)
    
    operations = fields.List(fields.Raw(required=False), required=False)
    
    enabled = fields.Boolean(required=False)
    

