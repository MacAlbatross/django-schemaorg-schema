# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WarrantyScopeSchema(SchemaObject):

    """Schema Mixin for WarrantyScope
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A range of of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.

    Commonly used values:

    http://purl.org/goodrelations/v1#Labor-BringIn 
    http://purl.org/goodrelations/v1#PartsAndLabor-BringIn 
    http://purl.org/goodrelations/v1#PartsAndLabor-PickUp 

    """

    def __init__(self):
        self.schema = 'WarrantyScope'


# schema.org version 2.0
