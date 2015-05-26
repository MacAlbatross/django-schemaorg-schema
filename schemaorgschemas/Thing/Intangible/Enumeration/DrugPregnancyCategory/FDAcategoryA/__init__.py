# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FDAcategoryASchema(SchemaObject):

    """Schema Mixin for FDAcategoryA
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A designation by the US FDA signifying that adequate and well-controlled studies have failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there is no evidence of risk in later trimesters).
    """

    def __init__(self):
        self.schema = 'FDAcategoryA'


# schema.org version 2.0
