# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TransferAction import fromLocationProp, toLocationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SendActionSchema(SchemaObject):

    """Schema Mixin for SendAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of physically/electronically dispatching an object for transfer from an origin to a destination.Related actions:ReceiveAction: The reciprocal of SendAction.GiveAction: Unlike GiveAction, SendAction does not imply the transfer of ownership (e.g. I can send you my laptop, but I&#39;m not necessarily giving it to you).
    """

    def __init__(self):
        self.schema = 'SendAction'


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


class deliveryMethodProp(SchemaProperty):

    """
    SchemaField for deliveryMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = deliveryMethodProp()  
    schema.org description:A sub property of instrument. The method of delivery

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DeliveryMethod"""

    _prop_schema = 'deliveryMethod'
    _expected_schema = 'DeliveryMethod'
    _enum = False
    _format_as = "ForeignKey"
