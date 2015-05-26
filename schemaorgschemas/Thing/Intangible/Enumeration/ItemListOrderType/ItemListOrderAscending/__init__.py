# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ItemListOrderAscendingSchema(SchemaObject):

    """Schema Mixin for ItemListOrderAscending
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An ItemList ordered with lower values listed first.
    """

    def __init__(self):
        self.schema = 'ItemListOrderAscending'


# schema.org version 2.0
