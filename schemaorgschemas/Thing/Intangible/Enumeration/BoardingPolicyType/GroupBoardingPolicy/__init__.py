# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GroupBoardingPolicySchema(SchemaObject):

    """Schema Mixin for GroupBoardingPolicy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The airline boards by groups based on check-in time, priority, etc.
    """

    def __init__(self):
        self.schema = 'GroupBoardingPolicy'


# schema.org version 2.0
