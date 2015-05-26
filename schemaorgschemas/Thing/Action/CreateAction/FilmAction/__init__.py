# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, resultProp, startTimeProp, errorProp, endTimeProp, locationProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class FilmActionSchema(SchemaObject):

    """Schema Mixin for FilmAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of capturing sound and moving images on film, video, or digitally.
    """

    def __init__(self):
        self.schema = 'FilmAction'


# schema.org version 2.0
