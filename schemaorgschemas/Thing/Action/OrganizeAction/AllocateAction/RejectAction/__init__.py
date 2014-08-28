# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing.Action.OrganizeAction.AllocateAction import purposeProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RejectActionSchema(SchemaObject):

    """Schema Mixin for RejectAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of rejecting to/adopting an object.Related actions:AcceptAction: The antagonym of RejectAction.
    """

    def __init__(self):
        self.schema = 'RejectAction'
