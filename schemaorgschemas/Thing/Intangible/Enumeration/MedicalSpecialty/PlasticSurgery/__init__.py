# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PlasticSurgerySchema(SchemaObject):

    """Schema Mixin for PlasticSurgery
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means.
    """

    def __init__(self):
        self.schema = 'PlasticSurgery'


# schema.org version 2.0
