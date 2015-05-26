# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MRISchema(SchemaObject):

    """Schema Mixin for MRI
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Magnetic resonance imaging.
    """

    def __init__(self):
        self.schema = 'MRI'


# schema.org version 2.0
