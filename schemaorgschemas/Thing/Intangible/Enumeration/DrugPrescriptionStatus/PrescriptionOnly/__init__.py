# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PrescriptionOnlySchema(SchemaObject):

    """Schema Mixin for PrescriptionOnly
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Available by prescription only.
    """

    def __init__(self):
        self.schema = 'PrescriptionOnly'


# schema.org version 2.0
