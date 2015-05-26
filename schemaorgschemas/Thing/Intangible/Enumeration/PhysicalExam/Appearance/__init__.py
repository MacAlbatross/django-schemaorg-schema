# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AppearanceSchema(SchemaObject):

    """Schema Mixin for Appearance
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Appearance.
    """

    def __init__(self):
        self.schema = 'Appearance'


# schema.org version 2.0
