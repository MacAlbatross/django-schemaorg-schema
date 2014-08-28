# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TransferAction import fromLocationProp, toLocationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DownloadActionSchema(SchemaObject):

    """Schema Mixin for DownloadAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of downloading an object.
    """

    def __init__(self):
        self.schema = 'DownloadAction'
