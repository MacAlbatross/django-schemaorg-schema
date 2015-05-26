# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DentistrySchema(SchemaObject):

    """Schema Mixin for Dentistry
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Dentistry.
    """

    def __init__(self):
        self.schema = 'Dentistry'


# schema.org version 2.0
