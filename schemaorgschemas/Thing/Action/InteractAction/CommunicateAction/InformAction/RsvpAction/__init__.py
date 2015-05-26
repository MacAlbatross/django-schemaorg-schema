# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction.InformAction import eventProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import inLanguageProp, aboutProp, recipientProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RsvpActionSchema(SchemaObject):

    """Schema Mixin for RsvpAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of notifying an event organizer as to whether you expect to attend the event.
    """

    def __init__(self):
        self.schema = 'RsvpAction'


class commentProp(SchemaProperty):

    """
    SchemaField for comment
    Usage: Include in SchemaObject SchemaFields as your_django_field = commentProp()  
    schema.org description:Comments, typically from users.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Comment"""

    _prop_schema = 'comment'
    _expected_schema = 'Comment'
    _enum = False
    _format_as = "ForeignKey"


class rsvpResponseProp(SchemaProperty):

    """
    SchemaField for rsvpResponse
    Usage: Include in SchemaObject SchemaFields as your_django_field = rsvpResponseProp()  
    schema.org description:The response (yes, no, maybe) to the RSVP.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference RsvpResponseType"""

    _prop_schema = 'rsvpResponse'
    _expected_schema = 'RsvpResponseType'
    _enum = False
    _format_as = "ForeignKey"


class additionalNumberOfGuestsProp(SchemaProperty):

    """
    SchemaField for additionalNumberOfGuests
    Usage: Include in SchemaObject SchemaFields as your_django_field = additionalNumberOfGuestsProp()  
    schema.org description:If responding yes, the number of guests who will attend in addition to the invitee.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Number"""

    _prop_schema = 'additionalNumberOfGuests'
    _expected_schema = 'Number'
    _enum = False
    _format_as = "FloatField"


# schema.org version 2.0
