# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SpokenWordAlbumSchema(SchemaObject):

    """Schema Mixin for SpokenWordAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    SpokenWordAlbum.
    """

    def __init__(self):
        self.schema = 'SpokenWordAlbum'


# schema.org version 2.0
