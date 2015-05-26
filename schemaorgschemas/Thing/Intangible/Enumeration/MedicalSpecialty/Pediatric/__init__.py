# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PediatricSchema(SchemaObject):

    """Schema Mixin for Pediatric
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific branch of medical science that specializes in the care of infants, children and adolescents.
    """

    def __init__(self):
        self.schema = 'Pediatric'


# schema.org version 2.0
