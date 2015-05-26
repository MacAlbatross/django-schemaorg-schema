# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FDAcategoryXSchema(SchemaObject):

    """Schema Mixin for FDAcategoryX
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A designation by the US FDA signifying that studies in animals or humans have demonstrated fetal abnormalities and/or there is positive evidence of human fetal risk based on adverse reaction data from investigational or marketing experience, and the risks involved in use of the drug in pregnant women clearly outweigh potential benefits.
    """

    def __init__(self):
        self.schema = 'FDAcategoryX'


# schema.org version 2.0
