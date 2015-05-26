# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ObstetricSchema(SchemaObject):

    """Schema Mixin for Obstetric
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child.
    """

    def __init__(self):
        self.schema = 'Obstetric'


# schema.org version 2.0
