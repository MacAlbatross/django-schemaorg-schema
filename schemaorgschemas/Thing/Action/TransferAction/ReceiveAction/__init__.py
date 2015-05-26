# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TransferAction import fromLocationProp, toLocationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReceiveActionSchema(SchemaObject):

    """Schema Mixin for ReceiveAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of physically/electronically taking delivery of an object thathas been transferred from an origin to a destination. Reciprocal of SendAction.Related actions:SendAction: The reciprocal of ReceiveAction.TakeAction: Unlike TakeAction, ReceiveAction does not imply that the ownership has been transfered (e.g. I can receive a package, but it does not mean the package is now mine).
    """

    def __init__(self):
        self.schema = 'ReceiveAction'


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


class senderProp(SchemaProperty):

    """
    SchemaField for sender
    Usage: Include in SchemaObject SchemaFields as your_django_field = senderProp()  
    schema.org description:A sub property of participant. The participant who is at the sending end of the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Audience"""

    _prop_schema = 'sender'
    _expected_schema = 'Audience'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
