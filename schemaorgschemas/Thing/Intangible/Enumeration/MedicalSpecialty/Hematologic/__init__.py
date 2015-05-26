# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class HematologicSchema(SchemaObject):

    """Schema Mixin for Hematologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.
    """

    def __init__(self):
        self.schema = 'Hematologic'


# schema.org version 2.0
