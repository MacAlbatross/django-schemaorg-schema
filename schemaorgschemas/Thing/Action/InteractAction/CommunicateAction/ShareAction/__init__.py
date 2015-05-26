# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.InteractAction.CommunicateAction import inLanguageProp, aboutProp, recipientProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ShareActionSchema(SchemaObject):

    """Schema Mixin for ShareAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of distributing content to people for their amusement or edification.
    """

    def __init__(self):
        self.schema = 'ShareAction'


# schema.org version 2.0
