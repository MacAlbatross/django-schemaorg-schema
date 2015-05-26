# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MultiCenterTrialSchema(SchemaObject):

    """Schema Mixin for MultiCenterTrial
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A trial that takes place at multiple centers.
    """

    def __init__(self):
        self.schema = 'MultiCenterTrial'


# schema.org version 2.0
