# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GastroenterologicSchema(SchemaObject):

    """Schema Mixin for Gastroenterologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to diagnosis and treatment of disorders of digestive system.
    """

    def __init__(self):
        self.schema = 'Gastroenterologic'


# schema.org version 2.0
