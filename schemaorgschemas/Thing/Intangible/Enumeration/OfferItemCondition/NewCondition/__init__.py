# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NewConditionSchema(SchemaObject):

    """Schema Mixin for NewCondition
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item is new.
    """

    def __init__(self):
        self.schema = 'NewCondition'


# schema.org version 2.0
