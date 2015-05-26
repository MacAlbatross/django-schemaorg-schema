# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GenitourinarySchema(SchemaObject):

    """Schema Mixin for Genitourinary
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Genitourinary.
    """

    def __init__(self):
        self.schema = 'Genitourinary'


# schema.org version 2.0
