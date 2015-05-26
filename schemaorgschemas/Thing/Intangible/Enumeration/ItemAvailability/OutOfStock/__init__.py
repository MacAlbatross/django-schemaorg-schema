# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OutOfStockSchema(SchemaObject):

    """Schema Mixin for OutOfStock
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is out of stock.
    """

    def __init__(self):
        self.schema = 'OutOfStock'


# schema.org version 2.0
