# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EventRescheduledSchema(SchemaObject):

    """Schema Mixin for EventRescheduled
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The event has been rescheduled. The event&#39;s previousStartDate should be set to the old date and the startDate should be set to the event&#39;s new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated).
    """

    def __init__(self):
        self.schema = 'EventRescheduled'


# schema.org version 2.0
