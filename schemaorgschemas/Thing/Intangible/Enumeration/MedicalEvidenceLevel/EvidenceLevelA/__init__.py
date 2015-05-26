# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EvidenceLevelASchema(SchemaObject):

    """Schema Mixin for EvidenceLevelA
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Data derived from multiple randomized clinical trials or meta-analyses.
    """

    def __init__(self):
        self.schema = 'EvidenceLevelA'


# schema.org version 2.0
