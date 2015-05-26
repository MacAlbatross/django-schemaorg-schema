# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderCancelledSchema(SchemaObject):

    """Schema Mixin for OrderCancelled
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    OrderStatus representing cancellation of an order.
    """

    def __init__(self):
        self.schema = 'OrderCancelled'


# schema.org version 2.0
