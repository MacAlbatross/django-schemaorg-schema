# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OnlineOnlySchema(SchemaObject):

    """Schema Mixin for OnlineOnly
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is available only online.
    """

    def __init__(self):
        self.schema = 'OnlineOnly'


# schema.org version 2.0
