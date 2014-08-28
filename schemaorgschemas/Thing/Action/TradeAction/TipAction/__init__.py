# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TradeAction import priceProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TipActionSchema(SchemaObject):

    """Schema Mixin for TipAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of giving money voluntarily to a beneficiary in recognition of services rendered.
    """

    def __init__(self):
        self.schema = 'TipAction'


class recipientProp(SchemaProperty):

    """
    SchemaField for recipient
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipientProp()  
    schema.org description:A sub property of participant. The participant who is at the receiving end of the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'recipient'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"
