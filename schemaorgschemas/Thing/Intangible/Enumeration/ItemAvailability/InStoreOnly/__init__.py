# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class InStoreOnlySchema(SchemaObject):

    """Schema Mixin for InStoreOnly
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is available only at physical locations.
    """

    def __init__(self):
        self.schema = 'InStoreOnly'


# schema.org version 2.0
