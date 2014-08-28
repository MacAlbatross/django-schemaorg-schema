# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction.InformAction import eventProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import aboutProp, recipientProp, languageProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RsvpActionSchema(SchemaObject):

    """Schema Mixin for RsvpAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of notifying an event organiser as to whether you expect to attend the event.
    """

    def __init__(self):
        self.schema = 'RsvpAction'
