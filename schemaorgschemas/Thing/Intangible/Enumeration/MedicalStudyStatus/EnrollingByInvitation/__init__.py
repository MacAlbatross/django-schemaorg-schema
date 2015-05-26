# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EnrollingByInvitationSchema(SchemaObject):

    """Schema Mixin for EnrollingByInvitation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Enrolling participants by invitation only.
    """

    def __init__(self):
        self.schema = 'EnrollingByInvitation'


# schema.org version 2.0
