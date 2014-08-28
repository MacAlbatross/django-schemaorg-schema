# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import aboutProp, recipientProp, languageProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReplyActionSchema(SchemaObject):

    """Schema Mixin for ReplyAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of responding to a question/message asked/sent by the object. Related to AskAction.Related actions:AskAction: Appears generally as an origin of a ReplyAction.
    """

    def __init__(self):
        self.schema = 'ReplyAction'
