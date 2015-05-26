# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FlexibilitySchema(SchemaObject):

    """Schema Mixin for Flexibility
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Physical activity that is engaged in to improve joint and muscle flexibility.
    """

    def __init__(self):
        self.schema = 'Flexibility'


# schema.org version 2.0
