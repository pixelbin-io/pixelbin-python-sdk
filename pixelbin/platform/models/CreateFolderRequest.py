"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CreateFolderRequest(BaseSchema):
    # Assets swagger.json

    
    name = fields.Str(required=False)
    
    path = fields.Str(required=False)
    

