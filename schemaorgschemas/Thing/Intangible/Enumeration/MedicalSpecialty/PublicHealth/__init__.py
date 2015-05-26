# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PublicHealthSchema(SchemaObject):

    """Schema Mixin for PublicHealth
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Environment and public health.
    """

    def __init__(self):
        self.schema = 'PublicHealth'


# schema.org version 2.0
