# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderProcessingSchema(SchemaObject):

    """Schema Mixin for OrderProcessing
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    OrderStatus representing that an order is being processed.
    """

    def __init__(self):
        self.schema = 'OrderProcessing'


# schema.org version 2.0
