# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FailedActionStatusSchema(SchemaObject):

    """Schema Mixin for FailedActionStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An action that failed to complete. The action&#39;s error property and the HTTP return code contain more information about the failure.
    """

    def __init__(self):
        self.schema = 'FailedActionStatus'


# schema.org version 2.0
