# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class StructuredValueSchema(SchemaObject):

    """Schema Mixin for StructuredValue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Structured values are strings-for example, addresses-that have certain constraints on their structure.
    """

    def __init__(self):
        self.schema = 'StructuredValue'
