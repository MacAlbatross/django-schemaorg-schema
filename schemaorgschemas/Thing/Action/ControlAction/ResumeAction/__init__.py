# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ResumeActionSchema(SchemaObject):

    """Schema Mixin for ResumeAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of resuming a device or application which was formerly paused (e.g. resume music playback or resume a timer).
    """

    def __init__(self):
        self.schema = 'ResumeAction'


# schema.org version 2.0
