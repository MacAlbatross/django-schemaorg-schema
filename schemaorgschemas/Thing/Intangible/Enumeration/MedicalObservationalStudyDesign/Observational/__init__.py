# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ObservationalSchema(SchemaObject):

    """Schema Mixin for Observational
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An observational study design.
    """

    def __init__(self):
        self.schema = 'Observational'


# schema.org version 2.0
