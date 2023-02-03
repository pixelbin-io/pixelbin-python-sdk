"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AddCredentialsRequest(BaseSchema):
    # Assets swagger.json

    
    credentials = fields.Dict(required=False)
    
    pluginId = fields.Str(required=False)
    

