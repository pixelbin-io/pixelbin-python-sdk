"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class AddPresetResponse(BaseSchema):
    # Assets swagger.json

    
    presetName = fields.Str(required=False)
    
    transformation = fields.Str(required=False)
    
    params = fields.Dict(required=False)
    
    archived = fields.Boolean(required=False)
    
    orgId = fields.Int(required=False)
    
    isActive = fields.Boolean(required=False)
    
    createdAt = fields.Str(required=False)
    
    updatedAt = fields.Str(required=False)
    

