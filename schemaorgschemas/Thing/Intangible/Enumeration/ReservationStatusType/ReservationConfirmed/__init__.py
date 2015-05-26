# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReservationConfirmedSchema(SchemaObject):

    """Schema Mixin for ReservationConfirmed
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The status of a confirmed reservation.
    """

    def __init__(self):
        self.schema = 'ReservationConfirmed'


# schema.org version 2.0
