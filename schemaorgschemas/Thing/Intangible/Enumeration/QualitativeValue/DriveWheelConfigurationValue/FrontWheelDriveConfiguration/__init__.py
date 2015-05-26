# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FrontWheelDriveConfigurationSchema(SchemaObject):

    """Schema Mixin for FrontWheelDriveConfiguration
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Front-wheel drive is a transmission layout where the engine drives the front wheels.
    """

    def __init__(self):
        self.schema = 'FrontWheelDriveConfiguration'


# schema.org version 2.0
