# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BroadcastReleaseSchema(SchemaObject):

    """Schema Mixin for BroadcastRelease
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    BroadcastRelease.
    """

    def __init__(self):
        self.schema = 'BroadcastRelease'


# schema.org version 2.0
