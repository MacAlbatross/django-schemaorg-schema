# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PhysiotherapySchema(SchemaObject):

    """Schema Mixin for Physiotherapy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Physiotherapy.
    """

    def __init__(self):
        self.schema = 'Physiotherapy'


# schema.org version 2.0
