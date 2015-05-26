# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReservationHoldSchema(SchemaObject):

    """Schema Mixin for ReservationHold
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The status of a reservation on hold pending an update like credit card number or flight changes.
    """

    def __init__(self):
        self.schema = 'ReservationHold'


# schema.org version 2.0
