# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReimbursementCapSchema(SchemaObject):

    """Schema Mixin for ReimbursementCap
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The drug&#39;s cost represents the maximum reimbursement paid by an insurer for the drug.
    """

    def __init__(self):
        self.schema = 'ReimbursementCap'


# schema.org version 2.0
