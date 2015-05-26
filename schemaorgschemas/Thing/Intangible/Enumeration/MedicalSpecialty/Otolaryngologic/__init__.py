# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OtolaryngologicSchema(SchemaObject):

    """Schema Mixin for Otolaryngologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states.
    """

    def __init__(self):
        self.schema = 'Otolaryngologic'


# schema.org version 2.0
