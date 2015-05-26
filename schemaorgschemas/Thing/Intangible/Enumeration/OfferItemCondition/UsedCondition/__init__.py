# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class UsedConditionSchema(SchemaObject):

    """Schema Mixin for UsedCondition
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is used.
    """

    def __init__(self):
        self.schema = 'UsedCondition'


# schema.org version 2.0
