# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AllWheelDriveConfigurationSchema(SchemaObject):

    """Schema Mixin for AllWheelDriveConfiguration
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    All-wheel Drive is a transmission layout where the engine drives all four wheels.
    """

    def __init__(self):
        self.schema = 'AllWheelDriveConfiguration'


# schema.org version 2.0
