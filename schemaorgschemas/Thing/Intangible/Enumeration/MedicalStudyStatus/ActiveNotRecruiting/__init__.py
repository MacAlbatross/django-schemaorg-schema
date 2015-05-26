# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ActiveNotRecruitingSchema(SchemaObject):

    """Schema Mixin for ActiveNotRecruiting
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Active, but not recruiting new participants.
    """

    def __init__(self):
        self.schema = 'ActiveNotRecruiting'


# schema.org version 2.0
