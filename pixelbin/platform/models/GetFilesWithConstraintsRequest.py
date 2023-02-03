"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetFilesWithConstraintsItem import GetFilesWithConstraintsItem






class GetFilesWithConstraintsRequest(BaseSchema):
    # Assets swagger.json

    
    items = fields.List(fields.Nested(GetFilesWithConstraintsItem, required=False), required=False)
    
    maxCount = fields.Float(required=False)
    
    maxSize = fields.Float(required=False)
    

