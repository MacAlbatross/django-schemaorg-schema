# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EvidenceLevelBSchema(SchemaObject):

    """Schema Mixin for EvidenceLevelB
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Data derived from a single randomized trial, or nonrandomized studies.
    """

    def __init__(self):
        self.schema = 'EvidenceLevelB'


# schema.org version 2.0
