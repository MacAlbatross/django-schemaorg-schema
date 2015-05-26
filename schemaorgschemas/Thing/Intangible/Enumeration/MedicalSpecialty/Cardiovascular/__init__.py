# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CardiovascularSchema(SchemaObject):

    """Schema Mixin for Cardiovascular
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to diagnosis and treatment of disorders of heart and vasculature.
    """

    def __init__(self):
        self.schema = 'Cardiovascular'


# schema.org version 2.0
