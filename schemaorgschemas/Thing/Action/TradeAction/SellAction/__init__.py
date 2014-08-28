# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TradeAction import priceProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SellActionSchema(SchemaObject):

    """Schema Mixin for SellAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of taking money from a buyer in exchange for goods or services rendered. An agent sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.
    """

    def __init__(self):
        self.schema = 'SellAction'


class buyerProp(SchemaProperty):

    """
    SchemaField for buyer
    Usage: Include in SchemaObject SchemaFields as your_django_field = buyerProp()  
    schema.org description:A sub property of participant. The participant/person/organization that bought the object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'buyer'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


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
