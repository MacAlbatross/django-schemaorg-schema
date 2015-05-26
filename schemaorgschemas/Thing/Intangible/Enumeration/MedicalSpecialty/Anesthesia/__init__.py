# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AnesthesiaSchema(SchemaObject):

    """Schema Mixin for Anesthesia
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to study of anesthetics and their application.
    """

    def __init__(self):
        self.schema = 'Anesthesia'


# schema.org version 2.0
