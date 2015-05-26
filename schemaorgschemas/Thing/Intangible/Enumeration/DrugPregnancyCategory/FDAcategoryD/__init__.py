# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FDAcategoryDSchema(SchemaObject):

    """Schema Mixin for FDAcategoryD
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A designation by the US FDA signifying that there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience or studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.
    """

    def __init__(self):
        self.schema = 'FDAcategoryD'


# schema.org version 2.0
