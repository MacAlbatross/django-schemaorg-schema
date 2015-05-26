# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TollFreeSchema(SchemaObject):

    """Schema Mixin for TollFree
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The associated telephone number is toll free.
    """

    def __init__(self):
        self.schema = 'TollFree'


# schema.org version 2.0
