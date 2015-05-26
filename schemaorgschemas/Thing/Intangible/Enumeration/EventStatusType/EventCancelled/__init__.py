# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EventCancelledSchema(SchemaObject):

    """Schema Mixin for EventCancelled
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event&#39;s cancelled date(s).
    """

    def __init__(self):
        self.schema = 'EventCancelled'


# schema.org version 2.0
