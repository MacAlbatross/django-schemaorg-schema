# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MidwiferySchema(SchemaObject):

    """Schema Mixin for Midwifery
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Midwifery.
    """

    def __init__(self):
        self.schema = 'Midwifery'


# schema.org version 2.0
