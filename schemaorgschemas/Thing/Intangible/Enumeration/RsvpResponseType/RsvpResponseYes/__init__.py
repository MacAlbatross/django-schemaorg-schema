# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RsvpResponseYesSchema(SchemaObject):

    """Schema Mixin for RsvpResponseYes
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The invitee will attend.
    """

    def __init__(self):
        self.schema = 'RsvpResponseYes'


# schema.org version 2.0
