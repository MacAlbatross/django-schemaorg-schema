# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RightHandDrivingSchema(SchemaObject):

    """Schema Mixin for RightHandDriving
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The steering position is on the right side of the vehicle (viewed from the main direction of driving).
    """

    def __init__(self):
        self.schema = 'RightHandDriving'


# schema.org version 2.0
