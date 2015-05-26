# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EventPostponedSchema(SchemaObject):

    """Schema Mixin for EventPostponed
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The event has been postponed and no new date has been set. The event&#39;s previousStartDate should be set.
    """

    def __init__(self):
        self.schema = 'EventPostponed'


# schema.org version 2.0
