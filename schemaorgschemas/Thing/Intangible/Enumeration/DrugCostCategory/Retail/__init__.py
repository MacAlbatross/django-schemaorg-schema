# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RetailSchema(SchemaObject):

    """Schema Mixin for Retail
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The drug&#39;s cost represents the retail cost of the drug.
    """

    def __init__(self):
        self.schema = 'Retail'


# schema.org version 2.0
