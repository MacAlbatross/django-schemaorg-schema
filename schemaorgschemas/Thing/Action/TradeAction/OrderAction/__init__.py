# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TradeAction import priceProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrderActionSchema(SchemaObject):

    """Schema Mixin for OrderAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An agent orders an object/product/service to be delivered/sent.
    """

    def __init__(self):
        self.schema = 'OrderAction'
