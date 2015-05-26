# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OsteopathicSchema(SchemaObject):

    """Schema Mixin for Osteopathic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A system of medicine focused on promoting the body&#39;s innate ability to heal itself.
    """

    def __init__(self):
        self.schema = 'Osteopathic'


# schema.org version 2.0
