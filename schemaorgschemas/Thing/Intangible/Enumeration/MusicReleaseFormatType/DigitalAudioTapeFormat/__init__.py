# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DigitalAudioTapeFormatSchema(SchemaObject):

    """Schema Mixin for DigitalAudioTapeFormat
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    DigitalAudioTapeFormat.
    """

    def __init__(self):
        self.schema = 'DigitalAudioTapeFormat'


# schema.org version 2.0
