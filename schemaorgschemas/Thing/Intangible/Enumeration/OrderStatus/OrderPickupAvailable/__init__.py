# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderPickupAvailableSchema(SchemaObject):

    """Schema Mixin for OrderPickupAvailable
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    OrderStatus representing availability of an order for pickup.
    """

    def __init__(self):
        self.schema = 'OrderPickupAvailable'


# schema.org version 2.0
