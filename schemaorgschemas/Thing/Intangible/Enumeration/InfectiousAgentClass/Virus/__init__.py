# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VirusSchema(SchemaObject):

    """Schema Mixin for Virus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Pathogenic virus that causes viral infection.
    """

    def __init__(self):
        self.schema = 'Virus'


# schema.org version 2.0
