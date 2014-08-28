# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CreditCardSchema(SchemaObject):

    """Schema Mixin for CreditCard
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A credit or debit card type as a standardized procedure for transferring the monetary amount for a purchase.

    Commonly used values:

    http://purl.org/goodrelations/v1#AmericanExpress
    http://purl.org/goodrelations/v1#DinersClub
    http://purl.org/goodrelations/v1#Discover
    http://purl.org/goodrelations/v1#JCB
    http://purl.org/goodrelations/v1#MasterCard
    http://purl.org/goodrelations/v1#VISA

    """

    def __init__(self):
        self.schema = 'CreditCard'
