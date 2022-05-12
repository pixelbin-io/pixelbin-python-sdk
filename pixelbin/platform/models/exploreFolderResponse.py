"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .folderItem import folderItem

from .exploreItem import exploreItem

from .page import page


class exploreFolderResponse(BaseSchema):
    # Assets swagger.json

    
    folder = fields.Nested(folderItem, required=False)
    
    items = fields.List(fields.Nested(exploreItem, required=False), required=False)
    
    page = fields.Nested(page, required=False)
    

