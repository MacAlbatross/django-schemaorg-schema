# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ApplyActionSchema(SchemaObject):

    """Schema Mixin for ApplyAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of registering to an organization/service without the guarantee to receive it. NOTE(goto): should this be under InteractAction instead?Related actions:RegisterAction: Unlike RegisterAction, ApplyAction has no guarantees that the application will be accepted.
    """

    def __init__(self):
        self.schema = 'ApplyAction'
