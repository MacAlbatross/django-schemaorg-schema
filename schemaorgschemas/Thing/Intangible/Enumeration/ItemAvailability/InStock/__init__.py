# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class InStockSchema(SchemaObject):

    """Schema Mixin for InStock
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is in stock.
    """

    def __init__(self):
        self.schema = 'InStock'


# schema.org version 2.0
