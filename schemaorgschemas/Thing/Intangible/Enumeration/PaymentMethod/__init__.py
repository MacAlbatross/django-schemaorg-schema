# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PaymentMethodSchema(SchemaObject):

    """Schema Mixin for PaymentMethod
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction.

    Commonly used values:

    http://purl.org/goodrelations/v1#ByBankTransferInAdvance 
    http://purl.org/goodrelations/v1#ByInvoice 
    http://purl.org/goodrelations/v1#Cash 
    http://purl.org/goodrelations/v1#CheckInAdvance 
    http://purl.org/goodrelations/v1#COD 
    http://purl.org/goodrelations/v1#DirectDebit 
    http://purl.org/goodrelations/v1#GoogleCheckout 
    http://purl.org/goodrelations/v1#PayPal 
    http://purl.org/goodrelations/v1#PaySwarm 

    """

    def __init__(self):
        self.schema = 'PaymentMethod'


# schema.org version 2.0
