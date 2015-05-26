# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PercutaneousProcedureSchema(SchemaObject):

    """Schema Mixin for PercutaneousProcedure
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A type of medical procedure that involves percutaneous techniques, where access to organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based procedures like stent delivery.
    """

    def __init__(self):
        self.schema = 'PercutaneousProcedure'


# schema.org version 2.0
