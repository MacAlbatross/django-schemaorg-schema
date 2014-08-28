# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import aboutProp, recipientProp, languageProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CheckInActionSchema(SchemaObject):

    """Schema Mixin for CheckInAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of an agent communicating (service provider, social media, etc) their arrival by registering/confirming for a previously reserved service (e.g. flight check in) or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc).Related actions:CheckOutAction: The antagonym of CheckInAction.ArriveAction: Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming the start of a previously reserved service.ConfirmAction: Unlike ConfirmAction, CheckInAction implies that the agent is informing/confirming the *start* of a previously reserved service rather than its validity/existance.
    """

    def __init__(self):
        self.schema = 'CheckInAction'
