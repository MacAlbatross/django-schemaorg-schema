# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WesternConventionalSchema(SchemaObject):

    """Schema Mixin for WesternConventional
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.
    """

    def __init__(self):
        self.schema = 'WesternConventional'


# schema.org version 2.0
