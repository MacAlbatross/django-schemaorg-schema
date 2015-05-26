# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ActiveActionStatusSchema(SchemaObject):

    """Schema Mixin for ActiveActionStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An in-progress action (e.g, while watching the movie, or driving to a location).
    """

    def __init__(self):
        self.schema = 'ActiveActionStatus'


# schema.org version 2.0
