# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import aboutProp, recipientProp, languageProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class InformActionSchema(SchemaObject):

    """Schema Mixin for InformAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of notifying someone of information pertinent to them, with no expectation of a response.
    """

    def __init__(self):
        self.schema = 'InformAction'


class eventProp(SchemaProperty):

    """
    SchemaField for event
    Usage: Include in SchemaObject SchemaFields as your_django_field = eventProp()
    schema.org description:Upcoming or past event associated with this place or organization. Supercedes events.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Event"""

    _prop_schema = 'event'
    _expected_schema = 'Event'
    _enum = False
    _format_as = "ForeignKey"
