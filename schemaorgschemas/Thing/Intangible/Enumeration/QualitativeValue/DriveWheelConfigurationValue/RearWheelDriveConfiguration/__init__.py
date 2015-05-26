# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RearWheelDriveConfigurationSchema(SchemaObject):

    """Schema Mixin for RearWheelDriveConfiguration
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Real-wheel drive is a transmission layout where the engine drives the rear wheels.
    """

    def __init__(self):
        self.schema = 'RearWheelDriveConfiguration'


# schema.org version 2.0
