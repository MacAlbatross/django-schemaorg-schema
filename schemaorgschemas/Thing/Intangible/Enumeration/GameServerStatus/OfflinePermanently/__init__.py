# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OfflinePermanentlySchema(SchemaObject):

    """Schema Mixin for OfflinePermanently
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Game server status: OfflinePermanently. Server is offline and not available.
    """

    def __init__(self):
        self.schema = 'OfflinePermanently'


# schema.org version 2.0
