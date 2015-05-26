# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RheumatologicSchema(SchemaObject):

    """Schema Mixin for Rheumatologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases.
    """

    def __init__(self):
        self.schema = 'Rheumatologic'


# schema.org version 2.0
