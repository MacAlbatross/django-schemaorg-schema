# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OptometicSchema(SchemaObject):

    """Schema Mixin for Optometic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Optometry.
    """

    def __init__(self):
        self.schema = 'Optometic'


# schema.org version 2.0
