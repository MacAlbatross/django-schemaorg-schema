# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DiscontinuedSchema(SchemaObject):

    """Schema Mixin for Discontinued
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item has been discontinued.
    """

    def __init__(self):
        self.schema = 'Discontinued'


# schema.org version 2.0
