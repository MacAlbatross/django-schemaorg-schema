# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LiveAlbumSchema(SchemaObject):

    """Schema Mixin for LiveAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    LiveAlbum.
    """

    def __init__(self):
        self.schema = 'LiveAlbum'


# schema.org version 2.0
