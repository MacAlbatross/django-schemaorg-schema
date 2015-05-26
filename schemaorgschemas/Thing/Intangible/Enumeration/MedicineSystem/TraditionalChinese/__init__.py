# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TraditionalChineseSchema(SchemaObject):

    """Schema Mixin for TraditionalChinese
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A system of medicine based on common theoretical concepts that originated in China and evolved over thousands of years, that uses herbs, acupuncture, exercise, massage, dietary therapy, and other methods to treat a wide range of conditions.
    """

    def __init__(self):
        self.schema = 'TraditionalChinese'


# schema.org version 2.0
