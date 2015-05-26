# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GeneticSchema(SchemaObject):

    """Schema Mixin for Genetic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders.
    """

    def __init__(self):
        self.schema = 'Genetic'


# schema.org version 2.0
