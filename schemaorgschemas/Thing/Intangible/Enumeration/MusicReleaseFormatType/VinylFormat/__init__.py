# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VinylFormatSchema(SchemaObject):

    """Schema Mixin for VinylFormat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    VinylFormat.
    """

    def __init__(self):
        self.schema = 'VinylFormat'


# schema.org version 2.0
