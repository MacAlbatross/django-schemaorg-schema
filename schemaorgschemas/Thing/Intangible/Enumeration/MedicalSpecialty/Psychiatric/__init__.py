# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PsychiatricSchema(SchemaObject):

    """Schema Mixin for Psychiatric
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.
    """

    def __init__(self):
        self.schema = 'Psychiatric'


# schema.org version 2.0
