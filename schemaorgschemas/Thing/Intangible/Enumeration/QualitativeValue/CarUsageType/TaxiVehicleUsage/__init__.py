# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TaxiVehicleUsageSchema(SchemaObject):

    """Schema Mixin for TaxiVehicleUsage
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates the usage of the car as a taxi.
    """

    def __init__(self):
        self.schema = 'TaxiVehicleUsage'


# schema.org version 2.0
