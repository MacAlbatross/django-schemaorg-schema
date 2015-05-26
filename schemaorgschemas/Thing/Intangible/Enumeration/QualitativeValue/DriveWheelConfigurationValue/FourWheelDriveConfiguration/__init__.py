# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FourWheelDriveConfigurationSchema(SchemaObject):

    """Schema Mixin for FourWheelDriveConfiguration
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel drive capability.
    """

    def __init__(self):
        self.schema = 'FourWheelDriveConfiguration'


# schema.org version 2.0
