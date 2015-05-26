# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ResultsAvailableSchema(SchemaObject):

    """Schema Mixin for ResultsAvailable
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Results are available.
    """

    def __init__(self):
        self.schema = 'ResultsAvailable'


# schema.org version 2.0
