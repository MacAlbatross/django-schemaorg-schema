# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SingleBlindedTrialSchema(SchemaObject):

    """Schema Mixin for SingleBlindedTrial
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not.
    """

    def __init__(self):
        self.schema = 'SingleBlindedTrial'


# schema.org version 2.0
