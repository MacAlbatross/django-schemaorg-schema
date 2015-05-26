# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OccupationalActivitySchema(SchemaObject):

    """Schema Mixin for OccupationalActivity
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any physical activity engaged in for job-related purposes. Examples may include waiting tables, maid service, carrying a mailbag, picking fruits or vegetables, construction work, etc.
    """

    def __init__(self):
        self.schema = 'OccupationalActivity'


# schema.org version 2.0
