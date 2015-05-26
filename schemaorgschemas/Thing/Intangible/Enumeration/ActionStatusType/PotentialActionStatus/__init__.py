# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PotentialActionStatusSchema(SchemaObject):

    """Schema Mixin for PotentialActionStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A description of an action that is supported.
    """

    def __init__(self):
        self.schema = 'PotentialActionStatus'


# schema.org version 2.0
