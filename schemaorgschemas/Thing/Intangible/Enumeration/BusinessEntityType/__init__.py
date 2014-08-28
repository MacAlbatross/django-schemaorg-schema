# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BusinessEntityTypeSchema(SchemaObject):

    """Schema Mixin for BusinessEntityType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A business entity type is a conceptual entity representing the legal form, the size, the main line of business, the position in the value chain, or any combination thereof, of an organization or business person.

    Commonly used values:

    http://purl.org/goodrelations/v1#Business
    http://purl.org/goodrelations/v1#Enduser
    http://purl.org/goodrelations/v1#PublicInstitution
    http://purl.org/goodrelations/v1#Reseller


    """

    def __init__(self):
        self.schema = 'BusinessEntityType'
