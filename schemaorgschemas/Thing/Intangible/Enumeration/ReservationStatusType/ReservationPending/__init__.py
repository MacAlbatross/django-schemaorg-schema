# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReservationPendingSchema(SchemaObject):

    """Schema Mixin for ReservationPending
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The status of a reservation when a request has been sent, but not confirmed.
    """

    def __init__(self):
        self.schema = 'ReservationPending'


# schema.org version 2.0
