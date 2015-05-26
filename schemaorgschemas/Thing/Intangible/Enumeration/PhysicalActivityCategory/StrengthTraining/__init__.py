# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class StrengthTrainingSchema(SchemaObject):

    """Schema Mixin for StrengthTraining
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Physical activity that is engaged in to improve muscle and bone strength. Also referred to as resistance training.
    """

    def __init__(self):
        self.schema = 'StrengthTraining'


# schema.org version 2.0
