# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.UpdateAction import collectionProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AddActionSchema(SchemaObject):

    """Schema Mixin for AddAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of editing by adding an object to a collection.
    """

    def __init__(self):
        self.schema = 'AddAction'
