"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class TransformationValidator:
    
    class getTransformationContext(BaseSchema):
        
        url = fields.Str(required=False)
         
    