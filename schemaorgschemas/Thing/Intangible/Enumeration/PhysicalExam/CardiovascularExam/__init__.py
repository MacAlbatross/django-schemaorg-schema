# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CardiovascularExamSchema(SchemaObject):

    """Schema Mixin for CardiovascularExam
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Cardiovascular.
    """

    def __init__(self):
        self.schema = 'CardiovascularExam'


# schema.org version 2.0
