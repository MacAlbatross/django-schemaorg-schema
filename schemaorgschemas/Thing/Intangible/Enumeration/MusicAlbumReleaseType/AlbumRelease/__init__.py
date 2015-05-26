# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AlbumReleaseSchema(SchemaObject):

    """Schema Mixin for AlbumRelease
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    AlbumRelease.
    """

    def __init__(self):
        self.schema = 'AlbumRelease'


# schema.org version 2.0
