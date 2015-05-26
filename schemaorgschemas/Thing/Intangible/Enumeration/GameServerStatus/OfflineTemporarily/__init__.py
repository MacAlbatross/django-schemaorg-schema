# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OfflineTemporarilySchema(SchemaObject):

    """Schema Mixin for OfflineTemporarily
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Game server status: OfflineTemporarily. Server is offline now but it can be online soon.
    """

    def __init__(self):
        self.schema = 'OfflineTemporarily'


# schema.org version 2.0
