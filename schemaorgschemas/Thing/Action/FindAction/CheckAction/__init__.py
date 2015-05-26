# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CheckActionSchema(SchemaObject):

    """Schema Mixin for CheckAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An agent inspects/determines/investigates/inquire or examine an object&#39;s accuracy/quality/condition or state.
    """

    def __init__(self):
        self.schema = 'CheckAction'


# schema.org version 2.0
