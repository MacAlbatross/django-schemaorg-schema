# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderInTransitSchema(SchemaObject):

    """Schema Mixin for OrderInTransit
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    OrderStatus representing that an order is in transit.
    """

    def __init__(self):
        self.schema = 'OrderInTransit'


# schema.org version 2.0
