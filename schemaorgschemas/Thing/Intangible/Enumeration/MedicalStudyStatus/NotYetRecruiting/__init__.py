# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NotYetRecruitingSchema(SchemaObject):

    """Schema Mixin for NotYetRecruiting
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Not yet recruiting.
    """

    def __init__(self):
        self.schema = 'NotYetRecruiting'


# schema.org version 2.0
