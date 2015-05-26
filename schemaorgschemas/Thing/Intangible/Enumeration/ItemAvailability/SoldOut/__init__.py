# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SoldOutSchema(SchemaObject):

    """Schema Mixin for SoldOut
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item has sold out.
    """

    def __init__(self):
        self.schema = 'SoldOut'


# schema.org version 2.0
