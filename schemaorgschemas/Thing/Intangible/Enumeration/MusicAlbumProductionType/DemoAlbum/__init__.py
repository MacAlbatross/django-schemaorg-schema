# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DemoAlbumSchema(SchemaObject):

    """Schema Mixin for DemoAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    DemoAlbum.
    """

    def __init__(self):
        self.schema = 'DemoAlbum'


# schema.org version 2.0
