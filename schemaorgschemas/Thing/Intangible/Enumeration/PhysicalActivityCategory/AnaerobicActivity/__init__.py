# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AnaerobicActivitySchema(SchemaObject):

    """Schema Mixin for AnaerobicActivity
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Physical activity that is of high-intensity which utilizes the anaerobic metabolism of the body.
    """

    def __init__(self):
        self.schema = 'AnaerobicActivity'


# schema.org version 2.0
