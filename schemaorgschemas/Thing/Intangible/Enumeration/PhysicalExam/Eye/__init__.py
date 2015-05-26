# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EyeSchema(SchemaObject):

    """Schema Mixin for Eye
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Eye.
    """

    def __init__(self):
        self.schema = 'Eye'


# schema.org version 2.0
