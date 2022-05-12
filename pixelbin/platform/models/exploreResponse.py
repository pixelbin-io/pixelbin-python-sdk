"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .exploreItem import exploreItem

from .page import page


class exploreResponse(BaseSchema):
    # Assets swagger.json

    
    items = fields.List(fields.Nested(exploreItem, required=False), required=False)
    
    page = fields.Nested(page, required=False)
    

