# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ItemListOrderDescendingSchema(SchemaObject):

    """Schema Mixin for ItemListOrderDescending
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An ItemList ordered with higher values listed first.
    """

    def __init__(self):
        self.schema = 'ItemListOrderDescending'


# schema.org version 2.0
