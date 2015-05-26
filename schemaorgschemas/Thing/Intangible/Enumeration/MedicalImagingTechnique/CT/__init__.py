# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CTSchema(SchemaObject):

    """Schema Mixin for CT
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    X-ray computed tomography imaging.
    """

    def __init__(self):
        self.schema = 'CT'


# schema.org version 2.0
