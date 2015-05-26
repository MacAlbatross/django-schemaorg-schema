# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PETSchema(SchemaObject):

    """Schema Mixin for PET
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Positron emission tomography imaging.
    """

    def __init__(self):
        self.schema = 'PET'


# schema.org version 2.0
