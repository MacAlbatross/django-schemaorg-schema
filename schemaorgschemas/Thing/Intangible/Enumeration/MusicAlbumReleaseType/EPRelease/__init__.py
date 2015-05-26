# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EPReleaseSchema(SchemaObject):

    """Schema Mixin for EPRelease
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    EPRelease.
    """

    def __init__(self):
        self.schema = 'EPRelease'


# schema.org version 2.0
