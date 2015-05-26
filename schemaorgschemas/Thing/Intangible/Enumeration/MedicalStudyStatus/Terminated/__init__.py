# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TerminatedSchema(SchemaObject):

    """Schema Mixin for Terminated
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Terminated.
    """

    def __init__(self):
        self.schema = 'Terminated'


# schema.org version 2.0
