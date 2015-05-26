# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OnlineSchema(SchemaObject):

    """Schema Mixin for Online
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Game server status: Online. Server is available.
    """

    def __init__(self):
        self.schema = 'Online'


# schema.org version 2.0
