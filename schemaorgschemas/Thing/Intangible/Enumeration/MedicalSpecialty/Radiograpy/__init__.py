# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RadiograpySchema(SchemaObject):

    """Schema Mixin for Radiograpy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Radiography.
    """

    def __init__(self):
        self.schema = 'Radiograpy'


# schema.org version 2.0
