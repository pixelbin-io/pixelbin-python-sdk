"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PresignedUrl import PresignedUrl


class SignedUploadResponse(BaseSchema):
    # Assets swagger.json

    
    s3PresignedUrl = fields.Nested(PresignedUrl, required=False)
    

