# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PlaceboControlledTrialSchema(SchemaObject):

    """Schema Mixin for PlaceboControlledTrial
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A placebo-controlled trial design.
    """

    def __init__(self):
        self.schema = 'PlaceboControlledTrial'


# schema.org version 2.0
