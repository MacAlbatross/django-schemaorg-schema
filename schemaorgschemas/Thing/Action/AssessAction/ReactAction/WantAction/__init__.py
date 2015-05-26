# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WantActionSchema(SchemaObject):

    """Schema Mixin for WantAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of expressing a desire about the object. An agent wants an object.
    """

    def __init__(self):
        self.schema = 'WantAction'


# schema.org version 2.0
