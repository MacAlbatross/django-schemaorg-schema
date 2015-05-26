# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WithdrawnSchema(SchemaObject):

    """Schema Mixin for Withdrawn
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Withdrawn.
    """

    def __init__(self):
        self.schema = 'Withdrawn'


# schema.org version 2.0
