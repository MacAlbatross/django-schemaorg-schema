# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OpenTrialSchema(SchemaObject):

    """Schema Mixin for OpenTrial
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A trial design in which the researcher knows the full details of the treatment, and so does the patient.
    """

    def __init__(self):
        self.schema = 'OpenTrial'


# schema.org version 2.0
