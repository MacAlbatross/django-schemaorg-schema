# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CommunityHealthSchema(SchemaObject):

    """Schema Mixin for CommunityHealth
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Community health.
    """

    def __init__(self):
        self.schema = 'CommunityHealth'


# schema.org version 2.0
