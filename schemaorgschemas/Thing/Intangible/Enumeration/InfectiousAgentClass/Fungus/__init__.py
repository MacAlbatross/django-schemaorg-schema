# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FungusSchema(SchemaObject):

    """Schema Mixin for Fungus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Pathogenic fungus.
    """

    def __init__(self):
        self.schema = 'Fungus'


# schema.org version 2.0
