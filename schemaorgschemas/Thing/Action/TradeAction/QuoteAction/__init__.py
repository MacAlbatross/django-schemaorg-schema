# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TradeAction import priceProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class QuoteActionSchema(SchemaObject):

    """Schema Mixin for QuoteAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An agent quotes/estimates/appraises an object/product/service with a price at a location/store.
    """

    def __init__(self):
        self.schema = 'QuoteAction'
