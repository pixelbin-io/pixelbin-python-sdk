"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class DeleteCredentialsResponse(BaseSchema):
    # Assets swagger.json

    
    _id = fields.Str(required=False)
    
    createdAt = fields.Str(required=False)
    
    updatedAt = fields.Str(required=False)
    
    isActive = fields.Boolean(required=False)
    
    orgId = fields.Str(required=False)
    
    pluginId = fields.Str(required=False)
    
    credentials = fields.Dict(required=False)
    

