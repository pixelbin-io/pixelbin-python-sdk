"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class GetTransformationContextSuccessResponse(BaseSchema):
    # Transformation swagger.json

    
    context = fields.Dict(required=False)
    

