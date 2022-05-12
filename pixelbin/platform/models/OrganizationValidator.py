"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

class OrganizationValidator:
    
    class getAppByToken(BaseSchema):
        
        token = fields.Str(required=False)
         
    