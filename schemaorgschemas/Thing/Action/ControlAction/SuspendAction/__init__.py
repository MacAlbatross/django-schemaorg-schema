# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SuspendActionSchema(SchemaObject):

    """Schema Mixin for SuspendAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of momentarily pausing a device or application (e.g. pause music playback or pause a timer).
    """

    def __init__(self):
        self.schema = 'SuspendAction'


# schema.org version 2.0
