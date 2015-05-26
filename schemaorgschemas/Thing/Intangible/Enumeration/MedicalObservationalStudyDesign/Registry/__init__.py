# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RegistrySchema(SchemaObject):

    """Schema Mixin for Registry
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A registry-based study design.
    """

    def __init__(self):
        self.schema = 'Registry'


# schema.org version 2.0
