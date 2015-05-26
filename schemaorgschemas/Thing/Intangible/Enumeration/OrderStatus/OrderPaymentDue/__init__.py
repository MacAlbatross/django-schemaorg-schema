# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderPaymentDueSchema(SchemaObject):

    """Schema Mixin for OrderPaymentDue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    OrderStatus representing that payment is due on an order.
    """

    def __init__(self):
        self.schema = 'OrderPaymentDue'


# schema.org version 2.0
