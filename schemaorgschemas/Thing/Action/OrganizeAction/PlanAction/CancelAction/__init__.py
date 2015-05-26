# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing.Action.OrganizeAction.PlanAction import scheduledTimeProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CancelActionSchema(SchemaObject):

    """Schema Mixin for CancelAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of asserting that a future event/action is no longer going to happen.Related actions:ConfirmAction: The antonym of CancelAction.
    """

    def __init__(self):
        self.schema = 'CancelAction'


# schema.org version 2.0
