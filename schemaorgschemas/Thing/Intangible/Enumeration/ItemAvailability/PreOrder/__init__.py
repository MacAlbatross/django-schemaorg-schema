# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PreOrderSchema(SchemaObject):

    """Schema Mixin for PreOrder
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is available for pre-order.
    """

    def __init__(self):
        self.schema = 'PreOrder'


# schema.org version 2.0
