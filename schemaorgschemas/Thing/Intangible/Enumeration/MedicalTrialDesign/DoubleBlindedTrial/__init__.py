# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DoubleBlindedTrialSchema(SchemaObject):

    """Schema Mixin for DoubleBlindedTrial
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A trial design in which neither the researcher nor the patient knows the details of the treatment the patient was randomly assigned to.
    """

    def __init__(self):
        self.schema = 'DoubleBlindedTrial'


# schema.org version 2.0
