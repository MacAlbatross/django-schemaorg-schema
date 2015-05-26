# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CDFormatSchema(SchemaObject):

    """Schema Mixin for CDFormat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    CDFormat.
    """

    def __init__(self):
        self.schema = 'CDFormat'


# schema.org version 2.0
