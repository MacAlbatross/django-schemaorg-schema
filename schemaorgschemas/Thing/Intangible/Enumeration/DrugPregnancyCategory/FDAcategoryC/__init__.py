# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FDAcategoryCSchema(SchemaObject):

    """Schema Mixin for FDAcategoryC
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A designation by the US FDA signifying that animal reproduction studies have shown an adverse effect on the fetus and there are no adequate and well-controlled studies in humans, but potential benefits may warrant use of the drug in pregnant women despite potential risks.
    """

    def __init__(self):
        self.schema = 'FDAcategoryC'


# schema.org version 2.0
