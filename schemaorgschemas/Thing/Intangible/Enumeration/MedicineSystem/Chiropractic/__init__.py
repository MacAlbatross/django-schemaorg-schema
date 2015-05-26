# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ChiropracticSchema(SchemaObject):

    """Schema Mixin for Chiropractic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A system of medicine focused on the relationship between the body&#39;s structure, mainly the spine, and its functioning.
    """

    def __init__(self):
        self.schema = 'Chiropractic'


# schema.org version 2.0
