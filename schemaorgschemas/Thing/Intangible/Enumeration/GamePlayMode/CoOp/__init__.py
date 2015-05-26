# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CoOpSchema(SchemaObject):

    """Schema Mixin for CoOp
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Play mode: CoOp. Co-operative games, where you play on the same team with friends.
    """

    def __init__(self):
        self.schema = 'CoOp'


# schema.org version 2.0
