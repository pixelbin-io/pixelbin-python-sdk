"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CredentialsItem(BaseSchema):
    # Assets swagger.json

    
    pluginId = fields.Raw(required=False)
    

