# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NoseSchema(SchemaObject):

    """Schema Mixin for Nose
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Nose.
    """

    def __init__(self):
        self.schema = 'Nose'


# schema.org version 2.0
