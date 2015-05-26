# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EventScheduledSchema(SchemaObject):

    """Schema Mixin for EventScheduled
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default.
    """

    def __init__(self):
        self.schema = 'EventScheduled'


# schema.org version 2.0
