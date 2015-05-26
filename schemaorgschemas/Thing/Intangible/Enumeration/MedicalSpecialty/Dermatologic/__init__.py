# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DermatologicSchema(SchemaObject):

    """Schema Mixin for Dermatologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to diagnosis and treatment of disorders of skin.
    """

    def __init__(self):
        self.schema = 'Dermatologic'


# schema.org version 2.0
