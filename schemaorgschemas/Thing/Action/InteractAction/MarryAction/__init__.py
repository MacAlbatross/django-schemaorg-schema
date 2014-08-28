# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MarryActionSchema(SchemaObject):

    """Schema Mixin for MarryAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of marrying a person.
    """

    def __init__(self):
        self.schema = 'MarryAction'
