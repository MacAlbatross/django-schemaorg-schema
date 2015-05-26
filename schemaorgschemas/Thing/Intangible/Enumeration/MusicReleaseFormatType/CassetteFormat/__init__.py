# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CassetteFormatSchema(SchemaObject):

    """Schema Mixin for CassetteFormat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    CassetteFormat.
    """

    def __init__(self):
        self.schema = 'CassetteFormat'


# schema.org version 2.0
