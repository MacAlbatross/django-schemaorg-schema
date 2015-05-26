# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RsvpResponseNoSchema(SchemaObject):

    """Schema Mixin for RsvpResponseNo
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The invitee will not attend.
    """

    def __init__(self):
        self.schema = 'RsvpResponseNo'


# schema.org version 2.0
