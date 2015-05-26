# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SkinSchema(SchemaObject):

    """Schema Mixin for Skin
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Skin.
    """

    def __init__(self):
        self.schema = 'Skin'


# schema.org version 2.0
