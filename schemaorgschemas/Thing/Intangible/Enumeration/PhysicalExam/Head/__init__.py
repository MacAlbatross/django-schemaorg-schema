# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class HeadSchema(SchemaObject):

    """Schema Mixin for Head
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Head.
    """

    def __init__(self):
        self.schema = 'Head'


# schema.org version 2.0
