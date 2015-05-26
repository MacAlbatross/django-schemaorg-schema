# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RenalSchema(SchemaObject):

    """Schema Mixin for Renal
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.
    """

    def __init__(self):
        self.schema = 'Renal'


# schema.org version 2.0
