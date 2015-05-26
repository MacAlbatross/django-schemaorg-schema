# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NeuroSchema(SchemaObject):

    """Schema Mixin for Neuro
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Neuro.
    """

    def __init__(self):
        self.schema = 'Neuro'


# schema.org version 2.0
