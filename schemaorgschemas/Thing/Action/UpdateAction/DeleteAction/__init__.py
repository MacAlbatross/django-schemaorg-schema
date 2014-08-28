# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.UpdateAction import collectionProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DeleteActionSchema(SchemaObject):

    """Schema Mixin for DeleteAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of editing a recipient by removing one of its objects.
    """

    def __init__(self):
        self.schema = 'DeleteAction'
