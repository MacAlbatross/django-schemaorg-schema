# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SurgicalSchema(SchemaObject):

    """Schema Mixin for Surgical
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.
    """

    def __init__(self):
        self.schema = 'Surgical'


# schema.org version 2.0
