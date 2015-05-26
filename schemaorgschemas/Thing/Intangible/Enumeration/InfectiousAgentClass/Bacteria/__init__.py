# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BacteriaSchema(SchemaObject):

    """Schema Mixin for Bacteria
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Pathogenic bacteria that cause bacterial infection.
    """

    def __init__(self):
        self.schema = 'Bacteria'


# schema.org version 2.0
