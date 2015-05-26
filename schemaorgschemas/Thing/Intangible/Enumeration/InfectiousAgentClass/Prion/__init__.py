# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PrionSchema(SchemaObject):

    """Schema Mixin for Prion
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A prion is an infectious agent composed of protein in a misfolded form.
    """

    def __init__(self):
        self.schema = 'Prion'


# schema.org version 2.0
