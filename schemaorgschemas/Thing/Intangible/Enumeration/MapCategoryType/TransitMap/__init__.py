# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TransitMapSchema(SchemaObject):

    """Schema Mixin for TransitMap
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A transit map.
    """

    def __init__(self):
        self.schema = 'TransitMap'


# schema.org version 2.0
