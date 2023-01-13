"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class UpdatePresetRequest(BaseSchema):
    # Assets swagger.json

    
    archived = fields.Boolean(required=False)
    

