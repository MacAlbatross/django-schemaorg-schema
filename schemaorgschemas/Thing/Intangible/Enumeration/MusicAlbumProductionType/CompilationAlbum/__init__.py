# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CompilationAlbumSchema(SchemaObject):

    """Schema Mixin for CompilationAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    CompilationAlbum.
    """

    def __init__(self):
        self.schema = 'CompilationAlbum'


# schema.org version 2.0
