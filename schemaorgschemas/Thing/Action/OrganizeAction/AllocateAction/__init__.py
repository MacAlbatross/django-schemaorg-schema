# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AllocateActionSchema(SchemaObject):

    """Schema Mixin for AllocateAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of organizing tasks/objects/events by associating resources to it.
    """

    def __init__(self):
        self.schema = 'AllocateAction'


class purposeProp(SchemaProperty):

    """
    SchemaField for purpose
    Usage: Include in SchemaObject SchemaFields as your_django_field = purposeProp()  
    schema.org description:A goal towards an action is taken. Can be concrete or abstract.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'purpose'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
