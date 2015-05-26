# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PatientSchema(SchemaObject):

    """Schema Mixin for Patient
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Patients.
    """

    def __init__(self):
        self.schema = 'Patient'


# schema.org version 2.0
