# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DVDFormatSchema(SchemaObject):

    """Schema Mixin for DVDFormat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    DVDFormat.
    """

    def __init__(self):
        self.schema = 'DVDFormat'


# schema.org version 2.0
