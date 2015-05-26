# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DigitalFormatSchema(SchemaObject):

    """Schema Mixin for DigitalFormat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    DigitalFormat.
    """

    def __init__(self):
        self.schema = 'DigitalFormat'


# schema.org version 2.0
