# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LaboratoryScienceSchema(SchemaObject):

    """Schema Mixin for LaboratoryScience
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Laboratory science.
    """

    def __init__(self):
        self.schema = 'LaboratoryScience'


# schema.org version 2.0
