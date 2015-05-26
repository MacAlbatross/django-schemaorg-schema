# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusculoskeletalExamSchema(SchemaObject):

    """Schema Mixin for MusculoskeletalExam
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Musculoskeletal.
    """

    def __init__(self):
        self.schema = 'MusculoskeletalExam'


# schema.org version 2.0
