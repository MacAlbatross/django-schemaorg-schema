# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FDAnotEvaluatedSchema(SchemaObject):

    """Schema Mixin for FDAnotEvaluated
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A designation that the drug in question has not been assigned a pregnancy category designation by the US FDA.
    """

    def __init__(self):
        self.schema = 'FDAnotEvaluated'


# schema.org version 2.0
