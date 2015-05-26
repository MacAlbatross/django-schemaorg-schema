# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NeurologicSchema(SchemaObject):

    """Schema Mixin for Neurologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that studies the nerves and nervous system and its respective disease states.
    """

    def __init__(self):
        self.schema = 'Neurologic'


# schema.org version 2.0
