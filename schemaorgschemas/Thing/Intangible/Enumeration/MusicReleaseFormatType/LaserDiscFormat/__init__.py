# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LaserDiscFormatSchema(SchemaObject):

    """Schema Mixin for LaserDiscFormat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    LaserDiscFormat.
    """

    def __init__(self):
        self.schema = 'LaserDiscFormat'


# schema.org version 2.0
