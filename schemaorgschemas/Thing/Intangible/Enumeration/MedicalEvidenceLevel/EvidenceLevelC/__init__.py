# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EvidenceLevelCSchema(SchemaObject):

    """Schema Mixin for EvidenceLevelC
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Only consensus opinion of experts, case studies, or standard-of-care.
    """

    def __init__(self):
        self.schema = 'EvidenceLevelC'


# schema.org version 2.0
