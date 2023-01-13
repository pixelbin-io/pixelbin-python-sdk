"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AddPresetResponse import AddPresetResponse

from .page import page


class GetPresetsResponse(BaseSchema):
    # Assets swagger.json

    
    items = fields.List(fields.Nested(AddPresetResponse, required=False), required=False)
    
    page = fields.Nested(page, required=False)
    

