# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DietNutritionSchema(SchemaObject):

    """Schema Mixin for DietNutrition
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Diet and nutrition.
    """

    def __init__(self):
        self.schema = 'DietNutrition'


# schema.org version 2.0
