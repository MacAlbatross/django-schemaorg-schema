# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OncologicSchema(SchemaObject):

    """Schema Mixin for Oncologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention.
    """

    def __init__(self):
        self.schema = 'Oncologic'


# schema.org version 2.0
