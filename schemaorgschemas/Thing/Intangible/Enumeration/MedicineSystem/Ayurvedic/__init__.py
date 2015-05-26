# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AyurvedicSchema(SchemaObject):

    """Schema Mixin for Ayurvedic
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A system of medicine that originated in India over thousands of years and that focuses on integrating and balancing the body, mind, and spirit.
    """

    def __init__(self):
        self.schema = 'Ayurvedic'


# schema.org version 2.0
