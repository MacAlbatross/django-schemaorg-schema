# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class UltrasoundSchema(SchemaObject):

    """Schema Mixin for Ultrasound
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Ultrasound imaging.
    """

    def __init__(self):
        self.schema = 'Ultrasound'


# schema.org version 2.0
