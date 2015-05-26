# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DamagedConditionSchema(SchemaObject):

    """Schema Mixin for DamagedCondition
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is damaged.
    """

    def __init__(self):
        self.schema = 'DamagedCondition'


# schema.org version 2.0
