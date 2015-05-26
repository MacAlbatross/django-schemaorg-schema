# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RecruitingSchema(SchemaObject):

    """Schema Mixin for Recruiting
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Recruiting participants.
    """

    def __init__(self):
        self.schema = 'Recruiting'


# schema.org version 2.0
