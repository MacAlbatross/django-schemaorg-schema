# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderProblemSchema(SchemaObject):

    """Schema Mixin for OrderProblem
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    OrderStatus representing that there is a problem with the order.
    """

    def __init__(self):
        self.schema = 'OrderProblem'


# schema.org version 2.0
