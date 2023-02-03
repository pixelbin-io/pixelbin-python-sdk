"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .folderItem import folderItem

from .FoldersResponse import FoldersResponse


class GetAncestorsResponse(BaseSchema):
    # Assets swagger.json

    
    folder = fields.Nested(folderItem, required=False)
    
    ancestors = fields.List(fields.Nested(FoldersResponse, required=False), required=False)
    

