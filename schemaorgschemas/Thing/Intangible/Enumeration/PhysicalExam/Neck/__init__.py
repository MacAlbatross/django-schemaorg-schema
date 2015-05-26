# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NeckSchema(SchemaObject):

    """Schema Mixin for Neck
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Neck.
    """

    def __init__(self):
        self.schema = 'Neck'


# schema.org version 2.0
