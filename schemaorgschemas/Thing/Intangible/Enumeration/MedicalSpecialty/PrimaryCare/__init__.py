# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PrimaryCareSchema(SchemaObject):

    """Schema Mixin for PrimaryCare
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Primary care.
    """

    def __init__(self):
        self.schema = 'PrimaryCare'


# schema.org version 2.0
