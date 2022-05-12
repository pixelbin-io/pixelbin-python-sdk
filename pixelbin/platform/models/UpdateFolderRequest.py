"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class UpdateFolderRequest(BaseSchema):
    # Assets swagger.json

    
    isActive = fields.Boolean(required=False)
    

