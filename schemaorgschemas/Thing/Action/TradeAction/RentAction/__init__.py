# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TradeAction import priceProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RentActionSchema(SchemaObject):

    """Schema Mixin for RentAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of giving money in return for temporary use, but not ownership, of an object such as a vehicle or property. For example, an agent rents a property from a landlord in exchange for a periodic payment.
    """

    def __init__(self):
        self.schema = 'RentAction'


class realEstateAgentProp(SchemaProperty):

    """
    SchemaField for realEstateAgent
    Usage: Include in SchemaObject SchemaFields as your_django_field = realEstateAgentProp()  
    schema.org description:A sub property of participant. The real estate agent involved in the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference RealEstateAgent"""

    _prop_schema = 'realEstateAgent'
    _expected_schema = 'RealEstateAgent'
    _enum = False
    _format_as = "ForeignKey"


class landlordProp(SchemaProperty):

    """
    SchemaField for landlord
    Usage: Include in SchemaObject SchemaFields as your_django_field = landlordProp()  
    schema.org description:A sub property of participant. The owner of the real estate property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'landlord'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"
