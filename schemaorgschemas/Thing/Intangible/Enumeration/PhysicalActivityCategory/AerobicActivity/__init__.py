# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AerobicActivitySchema(SchemaObject):

    """Schema Mixin for AerobicActivity
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Physical activity of relatively low intensity that depends primarily on the aerobic energy-generating process; during activity, the aerobic metabolism uses oxygen to adequately meet energy demands during exercise.
    """

    def __init__(self):
        self.schema = 'AerobicActivity'


# schema.org version 2.0
