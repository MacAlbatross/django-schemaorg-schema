# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ControlActionSchema(SchemaObject):

    """Schema Mixin for ControlAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An agent controls a device or application.
    """

    def __init__(self):
        self.schema = 'ControlAction'


# schema.org version 2.0
