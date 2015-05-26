# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SeatingMapSchema(SchemaObject):

    """Schema Mixin for SeatingMap
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A seating map.
    """

    def __init__(self):
        self.schema = 'SeatingMap'


# schema.org version 2.0
