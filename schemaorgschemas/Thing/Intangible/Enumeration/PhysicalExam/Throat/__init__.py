# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ThroatSchema(SchemaObject):

    """Schema Mixin for Throat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Throat.
    """

    def __init__(self):
        self.schema = 'Throat'


# schema.org version 2.0
