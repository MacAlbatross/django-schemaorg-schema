# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SuspendedSchema(SchemaObject):

    """Schema Mixin for Suspended
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Suspended.
    """

    def __init__(self):
        self.schema = 'Suspended'


# schema.org version 2.0
