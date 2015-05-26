# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ClinicianSchema(SchemaObject):

    """Schema Mixin for Clinician
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.
    """

    def __init__(self):
        self.schema = 'Clinician'


# schema.org version 2.0
