# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LongitudinalSchema(SchemaObject):

    """Schema Mixin for Longitudinal
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Unlike cross-sectional studies, longitudinal studies track the same people, and therefore the differences observed in those people are less likely to be the result of cultural differences across generations. Longitudinal studies are also used in medicine to uncover predictors of certain diseases.
    """

    def __init__(self):
        self.schema = 'Longitudinal'


# schema.org version 2.0
