# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RemixAlbumSchema(SchemaObject):

    """Schema Mixin for RemixAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    RemixAlbum.
    """

    def __init__(self):
        self.schema = 'RemixAlbum'


# schema.org version 2.0
