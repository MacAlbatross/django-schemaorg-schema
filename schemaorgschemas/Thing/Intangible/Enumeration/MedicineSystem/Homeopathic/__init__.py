# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class HomeopathicSchema(SchemaObject):

    """Schema Mixin for Homeopathic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.
    """

    def __init__(self):
        self.schema = 'Homeopathic'


# schema.org version 2.0
