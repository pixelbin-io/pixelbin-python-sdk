"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PresignedUrlV2 import PresignedUrlV2


class SignedUploadV2Response(BaseSchema):
    # Assets swagger.json

    
    presignedUrl = fields.Nested(PresignedUrlV2, required=False)
    

