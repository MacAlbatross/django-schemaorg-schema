# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LikeActionSchema(SchemaObject):

    """Schema Mixin for LikeAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of expressing a positive sentiment about the object. An agent likes an object (a proposition, topic or theme) with participants.
    """

    def __init__(self):
        self.schema = 'LikeAction'


# schema.org version 2.0
