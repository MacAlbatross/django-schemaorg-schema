# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TradeAction import priceProp, priceSpecificationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BuyActionSchema(SchemaObject):

    """Schema Mixin for BuyAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of giving money to a seller in exchange for goods or services rendered. An agent buys an object, product, or service from a seller for a price. Reciprocal of SellAction.
    """

    def __init__(self):
        self.schema = 'BuyAction'


class sellerProp(SchemaProperty):

    """
    SchemaField for seller
    Usage: Include in SchemaObject SchemaFields as your_django_field = sellerProp()  
    schema.org description:An entity which offers (sells / leases / lends / loans) the services / goods. A seller may also be a provider. Supersedes vendor, merchant.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'seller'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
