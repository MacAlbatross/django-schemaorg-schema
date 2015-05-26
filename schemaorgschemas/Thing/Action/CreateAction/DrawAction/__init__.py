# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrawActionSchema(SchemaObject):

    """Schema Mixin for DrawAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of producing a visual/graphical representation of an object, typically with a pen/pencil and paper as instruments.
    """

    def __init__(self):
        self.schema = 'DrawAction'


# schema.org version 2.0
