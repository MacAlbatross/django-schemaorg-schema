# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderReturnedSchema(SchemaObject):

    """Schema Mixin for OrderReturned
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    OrderStatus representing that an order has been returned.
    """

    def __init__(self):
        self.schema = 'OrderReturned'


# schema.org version 2.0
