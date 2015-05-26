# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ResultsNotAvailableSchema(SchemaObject):

    """Schema Mixin for ResultsNotAvailable
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Results are not available.
    """

    def __init__(self):
        self.schema = 'ResultsNotAvailable'


# schema.org version 2.0
