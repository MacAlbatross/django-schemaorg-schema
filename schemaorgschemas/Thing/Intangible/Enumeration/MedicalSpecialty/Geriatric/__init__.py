# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GeriatricSchema(SchemaObject):

    """Schema Mixin for Geriatric
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.
    """

    def __init__(self):
        self.schema = 'Geriatric'


# schema.org version 2.0
