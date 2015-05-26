# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TripleBlindedTrialSchema(SchemaObject):

    """Schema Mixin for TripleBlindedTrial
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to.
    """

    def __init__(self):
        self.schema = 'TripleBlindedTrial'


# schema.org version 2.0
