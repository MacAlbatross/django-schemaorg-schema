# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class HearingImpairedSupportedSchema(SchemaObject):

    """Schema Mixin for HearingImpairedSupported
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Uses devices to support users with hearing impairments.
    """

    def __init__(self):
        self.schema = 'HearingImpairedSupported'


# schema.org version 2.0
