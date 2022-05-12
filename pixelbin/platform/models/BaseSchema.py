"""Base Schema for Serializers."""

from marshmallow import EXCLUDE, Schema


class BaseSchema(Schema):
    """Base Schema for marshmallow."""
    class Meta:
        """Meta to not throw error on unknown keys."""
        unknown = EXCLUDE
