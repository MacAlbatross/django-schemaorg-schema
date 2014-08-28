# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class UnRegisterActionSchema(SchemaObject):

    """Schema Mixin for UnRegisterAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of un-registering from a service.Related actions:RegisterAction: Antagonym of UnRegisterAction.Leave: Unlike LeaveAction, UnRegisterAction implies that you are unregistering from a service you werer previously registered, rather than leaving a team/group of people.
    """

    def __init__(self):
        self.schema = 'UnRegisterAction'
