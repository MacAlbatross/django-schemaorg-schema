# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CompletedSchema(SchemaObject):

    """Schema Mixin for Completed
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Completed.
    """

    def __init__(self):
        self.schema = 'Completed'


# schema.org version 2.0
