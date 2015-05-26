# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MixtapeAlbumSchema(SchemaObject):

    """Schema Mixin for MixtapeAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    MixtapeAlbum.
    """

    def __init__(self):
        self.schema = 'MixtapeAlbum'


# schema.org version 2.0
