"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class FoldersResponse(BaseSchema):
    # Assets swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    isActive = fields.Boolean(required=False)
    

