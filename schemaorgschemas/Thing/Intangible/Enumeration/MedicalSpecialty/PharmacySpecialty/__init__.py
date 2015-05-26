# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PharmacySpecialtySchema(SchemaObject):

    """Schema Mixin for PharmacySpecialty
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Pharmacy.
    """

    def __init__(self):
        self.schema = 'PharmacySpecialty'


# schema.org version 2.0
