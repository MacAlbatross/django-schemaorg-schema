# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SurgicalProcedureSchema(SchemaObject):

    """Schema Mixin for SurgicalProcedure
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A type of medical procedure that involves invasive surgical techniques.
    """

    def __init__(self):
        self.schema = 'SurgicalProcedure'


# schema.org version 2.0
