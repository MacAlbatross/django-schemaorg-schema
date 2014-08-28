# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ClassSchema(SchemaObject):

    """Schema Mixin for Class
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A class, also often called a &#39;Type&#39;; equivalent to rdfs:Class.
    """

    def __init__(self):
        self.schema = 'Class'
