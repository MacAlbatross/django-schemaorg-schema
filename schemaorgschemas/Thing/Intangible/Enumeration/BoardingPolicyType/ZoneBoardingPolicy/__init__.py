# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ZoneBoardingPolicySchema(SchemaObject):

    """Schema Mixin for ZoneBoardingPolicy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The airline boards by zones of the plane.
    """

    def __init__(self):
        self.schema = 'ZoneBoardingPolicy'


# schema.org version 2.0
