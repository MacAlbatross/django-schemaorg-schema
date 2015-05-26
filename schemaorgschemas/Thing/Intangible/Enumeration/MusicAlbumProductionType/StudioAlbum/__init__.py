# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class StudioAlbumSchema(SchemaObject):

    """Schema Mixin for StudioAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    StudioAlbum.
    """

    def __init__(self):
        self.schema = 'StudioAlbum'


# schema.org version 2.0
