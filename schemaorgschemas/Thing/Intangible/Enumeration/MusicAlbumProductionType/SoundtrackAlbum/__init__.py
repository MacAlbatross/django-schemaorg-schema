# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SoundtrackAlbumSchema(SchemaObject):

    """Schema Mixin for SoundtrackAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    SoundtrackAlbum.
    """

    def __init__(self):
        self.schema = 'SoundtrackAlbum'


# schema.org version 2.0
