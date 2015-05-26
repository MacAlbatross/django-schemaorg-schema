# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RsvpResponseTypeSchema(SchemaObject):

    """Schema Mixin for RsvpResponseType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.
    """

    def __init__(self):
        self.schema = 'RsvpResponseType'


RSVPRESPONSE_CHOICES = (
    ('RSVPRESPONSENO', 'RsvpResponseNo: The invitee will not attend.'),
    ('RSVPRESPONSEYES', 'RsvpResponseYes: The invitee will attend.'),
    ('RSVPRESPONSEMAYBE',
     'RsvpResponseMaybe: The invitee may or may not attend.'),
)


class rsvpResponseProp(SchemaEnumProperty):

    """
    Enumeration for rsvpResponse
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'rsvpResponse'
    choices = RSVPRESPONSE_CHOICES
    _format_as = "enum"
    adapter = {
        'RSVPRESPONSENO': 'RsvpResponseNo',
        'RSVPRESPONSEYES': 'RsvpResponseYes',
        'RSVPRESPONSEMAYBE': 'RsvpResponseMaybe',
    }


# schema.org version 2.0
