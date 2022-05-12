"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class page(BaseSchema):
    # Assets swagger.json

    
    type = fields.Str(required=False)
    
    size = fields.Int(required=False)
    
    current = fields.Int(required=False)
    
    hasNext = fields.Boolean(required=False)
    
    itemTotal = fields.Int(required=False)
    

