# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FDAcategoryBSchema(SchemaObject):

    """Schema Mixin for FDAcategoryB
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A designation by the US FDA signifying that animal reproduction studies have failed to demonstrate a risk to the fetus and there are no adequate and well-controlled studies in pregnant women.
    """

    def __init__(self):
        self.schema = 'FDAcategoryB'


# schema.org version 2.0
