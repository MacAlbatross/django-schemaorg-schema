# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TherapeuticSchema(SchemaObject):

    """Schema Mixin for Therapeutic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A medical device used for therapeutic purposes.
    """

    def __init__(self):
        self.schema = 'Therapeutic'


# schema.org version 2.0
