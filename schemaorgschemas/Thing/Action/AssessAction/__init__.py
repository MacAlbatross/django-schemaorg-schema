# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AssessActionSchema(SchemaObject):

    """Schema Mixin for AssessAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of forming one&#39;s opinion, reaction or sentiment.
    """

    def __init__(self):
        self.schema = 'AssessAction'


# schema.org version 2.0
