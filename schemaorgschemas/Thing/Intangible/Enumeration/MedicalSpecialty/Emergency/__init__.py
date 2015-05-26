# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EmergencySchema(SchemaObject):

    """Schema Mixin for Emergency
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that is deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.
    """

    def __init__(self):
        self.schema = 'Emergency'


# schema.org version 2.0
