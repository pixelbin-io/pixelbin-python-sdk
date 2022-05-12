"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Delimiter(BaseSchema):
    # Assets swagger.json

    
    operationSeparator = fields.Str(required=False)
    
    parameterSeparator = fields.Str(required=False)
    

