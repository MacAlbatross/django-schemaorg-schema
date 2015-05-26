# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrivingSchoolVehicleUsageSchema(SchemaObject):

    """Schema Mixin for DrivingSchoolVehicleUsage
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates the usage of the vehicle for driving school.
    """

    def __init__(self):
        self.schema = 'DrivingSchoolVehicleUsage'


# schema.org version 2.0
