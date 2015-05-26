# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PodiatricSchema(SchemaObject):

    """Schema Mixin for Podiatric
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Podiatry.
    """

    def __init__(self):
        self.schema = 'Podiatric'


# schema.org version 2.0
