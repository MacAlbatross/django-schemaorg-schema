# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ParkingMapSchema(SchemaObject):

    """Schema Mixin for ParkingMap
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A parking map.
    """

    def __init__(self):
        self.schema = 'ParkingMap'


# schema.org version 2.0
