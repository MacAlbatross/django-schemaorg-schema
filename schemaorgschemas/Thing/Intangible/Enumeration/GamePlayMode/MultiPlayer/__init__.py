# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MultiPlayerSchema(SchemaObject):

    """Schema Mixin for MultiPlayer
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.
    """

    def __init__(self):
        self.schema = 'MultiPlayer'


# schema.org version 2.0
