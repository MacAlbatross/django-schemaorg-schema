# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.MoveAction import fromLocationProp, toLocationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DepartActionSchema(SchemaObject):

    """Schema Mixin for DepartAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of  departing from a place. An agent departs from an fromLocation for a destination, optionally with participants.
    """

    def __init__(self):
        self.schema = 'DepartAction'


# schema.org version 2.0
