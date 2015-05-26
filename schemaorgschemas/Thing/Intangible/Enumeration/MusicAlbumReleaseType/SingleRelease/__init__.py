# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SingleReleaseSchema(SchemaObject):

    """Schema Mixin for SingleRelease
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    SingleRelease.
    """

    def __init__(self):
        self.schema = 'SingleRelease'


# schema.org version 2.0
