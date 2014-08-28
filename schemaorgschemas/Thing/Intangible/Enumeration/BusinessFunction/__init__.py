# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BusinessFunctionSchema(SchemaObject):

    """Schema Mixin for BusinessFunction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The business function specifies the type of activity or access (i.e., the bundle of rights) offered by the organization or business person through the offer. Typical are sell, rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering / construction, or installation. Proprietary specifications of access rights are also instances of this class.

    Commonly used values:

    http://purl.org/goodrelations/v1#ConstructionInstallation
    http://purl.org/goodrelations/v1#Dispose
    http://purl.org/goodrelations/v1#LeaseOut
    http://purl.org/goodrelations/v1#Maintain
    http://purl.org/goodrelations/v1#ProvideService
    http://purl.org/goodrelations/v1#Repair
    http://purl.org/goodrelations/v1#Sell
    http://purl.org/goodrelations/v1#Buy

    """

    def __init__(self):
        self.schema = 'BusinessFunction'
