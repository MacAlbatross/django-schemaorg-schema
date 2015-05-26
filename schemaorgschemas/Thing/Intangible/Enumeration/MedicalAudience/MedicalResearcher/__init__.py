# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalResearcherSchema(SchemaObject):

    """Schema Mixin for MedicalResearcher
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Medical researchers.
    """

    def __init__(self):
        self.schema = 'MedicalResearcher'


# schema.org version 2.0
