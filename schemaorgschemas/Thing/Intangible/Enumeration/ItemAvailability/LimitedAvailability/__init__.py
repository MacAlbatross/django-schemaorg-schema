# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LimitedAvailabilitySchema(SchemaObject):

    """Schema Mixin for LimitedAvailability
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates that the item has limited availability.
    """

    def __init__(self):
        self.schema = 'LimitedAvailability'


# schema.org version 2.0
