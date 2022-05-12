"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class AppSchema(BaseSchema):
    # Organization swagger.json

    
    _id = fields.Int(required=False)
    
    orgId = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    permissions = fields.List(fields.Str(required=False), required=False)
    
    active = fields.Boolean(required=False)
    
    createdAt = fields.Str(required=False)
    
    updatedAt = fields.Str(required=False)
    

