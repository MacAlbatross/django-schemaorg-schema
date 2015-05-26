# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LeftHandDrivingSchema(SchemaObject):

    """Schema Mixin for LeftHandDriving
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The steering position is on the left side of the vehicle (viewed from the main direction of driving).
    """

    def __init__(self):
        self.schema = 'LeftHandDriving'


# schema.org version 2.0
