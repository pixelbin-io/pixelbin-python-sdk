"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class OrganizationDetailSchema(BaseSchema):
    # Organization swagger.json

    
    _id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    cloudName = fields.Str(required=False)
    
    ownerId = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    createdAt = fields.Str(required=False)
    
    updatedAt = fields.Str(required=False)
    

