# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RsvpResponseMaybeSchema(SchemaObject):

    """Schema Mixin for RsvpResponseMaybe
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The invitee may or may not attend.
    """

    def __init__(self):
        self.schema = 'RsvpResponseMaybe'


# schema.org version 2.0
