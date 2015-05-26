# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RespiratoryTherapySchema(SchemaObject):

    """Schema Mixin for RespiratoryTherapy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Respiratory therapy.
    """

    def __init__(self):
        self.schema = 'RespiratoryTherapy'


# schema.org version 2.0
