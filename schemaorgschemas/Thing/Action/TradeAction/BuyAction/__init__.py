# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TradeAction import priceProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BuyActionSchema(SchemaObject):

    """Schema Mixin for BuyAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product, or service from a seller for a price. Reciprocal of SellAction.
    """

    def __init__(self):
        self.schema = 'BuyAction'


class warrantyPromiseProp(SchemaProperty):

    """
    SchemaField for warrantyPromise
    Usage: Include in SchemaObject SchemaFields as your_django_field = warrantyPromiseProp()  
    schema.org description:The warranty promise(s) included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference WarrantyPromise"""

    _prop_schema = 'warrantyPromise'
    _expected_schema = 'WarrantyPromise'
    _enum = False
    _format_as = "ForeignKey"


class vendorProp(SchemaProperty):

    """
    SchemaField for vendor
    Usage: Include in SchemaObject SchemaFields as your_django_field = vendorProp()  
    schema.org description:A sub property of participant. The seller. The participant/person/organization that sold the object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'vendor'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"
