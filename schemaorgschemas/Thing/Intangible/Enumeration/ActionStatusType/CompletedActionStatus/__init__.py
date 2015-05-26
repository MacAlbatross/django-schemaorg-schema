# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CompletedActionStatusSchema(SchemaObject):

    """Schema Mixin for CompletedActionStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An action that has already taken place.
    """

    def __init__(self):
        self.schema = 'CompletedActionStatus'


# schema.org version 2.0
