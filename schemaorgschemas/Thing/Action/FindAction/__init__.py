# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FindActionSchema(SchemaObject):

    """Schema Mixin for FindAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of finding an object.Related actions:SearchAction: FindAction is generally lead by a SearchAction, but not necessarily.
    """

    def __init__(self):
        self.schema = 'FindAction'


# schema.org version 2.0
