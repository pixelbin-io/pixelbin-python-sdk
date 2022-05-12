"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppSchema import AppSchema

from .OrganizationDetailSchema import OrganizationDetailSchema


class AppDetailsByToken(BaseSchema):
    # Organization swagger.json

    
    app = fields.Nested(AppSchema, required=False)
    
    org = fields.Nested(OrganizationDetailSchema, required=False)
    

