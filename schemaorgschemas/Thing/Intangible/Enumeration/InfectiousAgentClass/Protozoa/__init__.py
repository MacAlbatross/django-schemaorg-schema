# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ProtozoaSchema(SchemaObject):

    """Schema Mixin for Protozoa
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Single-celled organism that causes an infection.
    """

    def __init__(self):
        self.schema = 'Protozoa'


# schema.org version 2.0
