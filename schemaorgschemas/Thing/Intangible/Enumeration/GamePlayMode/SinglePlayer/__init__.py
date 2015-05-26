# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SinglePlayerSchema(SchemaObject):

    """Schema Mixin for SinglePlayer
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Play mode: SinglePlayer. Which is played by a lone player.
    """

    def __init__(self):
        self.schema = 'SinglePlayer'


# schema.org version 2.0
