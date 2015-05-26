# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PulmonarySchema(SchemaObject):

    """Schema Mixin for Pulmonary
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states.
    """

    def __init__(self):
        self.schema = 'Pulmonary'


# schema.org version 2.0
