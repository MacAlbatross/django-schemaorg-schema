# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WholesaleSchema(SchemaObject):

    """Schema Mixin for Wholesale
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The drug&#39;s cost represents the wholesale acquisition cost of the drug.
    """

    def __init__(self):
        self.schema = 'Wholesale'


# schema.org version 2.0
