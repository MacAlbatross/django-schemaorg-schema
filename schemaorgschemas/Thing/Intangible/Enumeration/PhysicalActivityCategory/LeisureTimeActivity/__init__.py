# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LeisureTimeActivitySchema(SchemaObject):

    """Schema Mixin for LeisureTimeActivity
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any physical activity engaged in for recreational purposes. Examples may include ballroom dancing, roller skating, canoeing, fishing, etc.
    """

    def __init__(self):
        self.schema = 'LeisureTimeActivity'


# schema.org version 2.0
