# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing.Action.OrganizeAction.PlanAction import scheduledTimeProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ScheduleActionSchema(SchemaObject):

    """Schema Mixin for ScheduleAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Scheduling future actions, events, or tasks.Related actions:ReserveAction: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.
    """

    def __init__(self):
        self.schema = 'ScheduleAction'
