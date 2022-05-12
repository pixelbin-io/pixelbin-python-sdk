"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PresignedUrl(BaseSchema):
    # Assets swagger.json

    
    url = fields.Str(required=False)
    
    fields = fields.Dict(required=False)
    

