# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BalanceSchema(SchemaObject):

    """Schema Mixin for Balance
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Physical activity that is engaged to help maintain posture and balance.
    """

    def __init__(self):
        self.schema = 'Balance'


# schema.org version 2.0
