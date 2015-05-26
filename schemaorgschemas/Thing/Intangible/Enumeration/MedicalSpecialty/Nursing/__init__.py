# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NursingSchema(SchemaObject):

    """Schema Mixin for Nursing
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Nursing.
    """

    def __init__(self):
        self.schema = 'Nursing'


# schema.org version 2.0
