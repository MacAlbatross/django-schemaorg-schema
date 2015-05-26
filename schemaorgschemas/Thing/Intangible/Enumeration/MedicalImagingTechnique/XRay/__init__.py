# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class XRaySchema(SchemaObject):

    """Schema Mixin for XRay
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    X-ray imaging.
    """

    def __init__(self):
        self.schema = 'XRay'


# schema.org version 2.0
