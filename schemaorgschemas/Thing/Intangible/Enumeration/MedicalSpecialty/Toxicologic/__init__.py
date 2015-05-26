# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ToxicologicSchema(SchemaObject):

    """Schema Mixin for Toxicologic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning.
    """

    def __init__(self):
        self.schema = 'Toxicologic'


# schema.org version 2.0
