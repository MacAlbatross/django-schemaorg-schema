# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, resultProp, startTimeProp, errorProp, endTimeProp, locationProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import inLanguageProp, aboutProp, recipientProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction.InformAction import eventProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ConfirmActionSchema(SchemaObject):

    """Schema Mixin for ConfirmAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of notifying someone that a future event/action is going to happen as expected.Related actions:CancelAction: The antonym of ConfirmAction.
    """

    def __init__(self):
        self.schema = 'ConfirmAction'


# schema.org version 2.0
