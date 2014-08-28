# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EnumerationSchema(SchemaObject):

    """Schema Mixin for Enumeration
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Lists or enumerations-for example, a list of cuisines or music genres, etc.
    """

    def __init__(self):
        self.schema = 'Enumeration'
