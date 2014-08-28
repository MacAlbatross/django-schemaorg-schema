# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TradeActionSchema(SchemaObject):

    """Schema Mixin for TradeAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.
    """

    def __init__(self):
        self.schema = 'TradeAction'


class priceProp(SchemaProperty):

    """
    SchemaField for price
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceProp()  
    schema.org description:The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'price'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"
