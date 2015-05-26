# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class HardcoverSchema(SchemaObject):

    """Schema Mixin for Hardcover
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Book format: Hardcover.
    """

    def __init__(self):
        self.schema = 'Hardcover'


# schema.org version 2.0
