# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RentalVehicleUsageSchema(SchemaObject):

    """Schema Mixin for RentalVehicleUsage
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates the usage of the vehicle as a rental car.
    """

    def __init__(self):
        self.schema = 'RentalVehicleUsage'


# schema.org version 2.0
