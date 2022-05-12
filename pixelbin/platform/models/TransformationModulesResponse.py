"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Delimiter import Delimiter






class TransformationModulesResponse(BaseSchema):
    # Assets swagger.json

    
    delimiters = fields.Nested(Delimiter, required=False)
    
    plugins = fields.Dict(required=False)
    
    presets = fields.List(fields.Raw(required=False), required=False)
    

