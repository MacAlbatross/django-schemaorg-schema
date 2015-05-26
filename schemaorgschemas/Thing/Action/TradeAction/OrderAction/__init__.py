# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, resultProp, startTimeProp, errorProp, endTimeProp, locationProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TradeAction import priceProp, priceSpecificationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderActionSchema(SchemaObject):

    """Schema Mixin for OrderAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An agent orders an object/product/service to be delivered/sent.
    """

    def __init__(self):
        self.schema = 'OrderAction'


class deliveryMethodProp(SchemaProperty):

    """
    SchemaField for deliveryMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = deliveryMethodProp()  
    schema.org description:A sub property of instrument. The method of delivery.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DeliveryMethod"""

    _prop_schema = 'deliveryMethod'
    _expected_schema = 'DeliveryMethod'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
