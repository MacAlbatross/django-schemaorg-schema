# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReservationCancelledSchema(SchemaObject):

    """Schema Mixin for ReservationCancelled
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The status for a previously confirmed reservation that is now cancelled.
    """

    def __init__(self):
        self.schema = 'ReservationCancelled'


# schema.org version 2.0
