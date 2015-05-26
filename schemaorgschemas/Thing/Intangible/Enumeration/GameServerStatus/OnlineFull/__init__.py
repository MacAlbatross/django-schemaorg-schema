# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OnlineFullSchema(SchemaObject):

    """Schema Mixin for OnlineFull
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.
    """

    def __init__(self):
        self.schema = 'OnlineFull'


# schema.org version 2.0
