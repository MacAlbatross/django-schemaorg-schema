# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AbdomenSchema(SchemaObject):

    """Schema Mixin for Abdomen
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Abdomen.
    """

    def __init__(self):
        self.schema = 'Abdomen'


# schema.org version 2.0
