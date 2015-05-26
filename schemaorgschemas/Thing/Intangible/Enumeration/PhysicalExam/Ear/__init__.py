# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EarSchema(SchemaObject):

    """Schema Mixin for Ear
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Ear.
    """

    def __init__(self):
        self.schema = 'Ear'


# schema.org version 2.0
