# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.OrganizeAction.AllocateAction import purposeProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AcceptActionSchema(SchemaObject):

    """Schema Mixin for AcceptAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of committing to/adopting an object.Related actions:RejectAction: The antonym of AcceptAction.
    """

    def __init__(self):
        self.schema = 'AcceptAction'


# schema.org version 2.0
