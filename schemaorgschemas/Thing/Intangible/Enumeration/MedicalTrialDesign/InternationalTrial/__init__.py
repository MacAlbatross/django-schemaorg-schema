# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class InternationalTrialSchema(SchemaObject):

    """Schema Mixin for InternationalTrial
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An international trial.
    """

    def __init__(self):
        self.schema = 'InternationalTrial'


# schema.org version 2.0
