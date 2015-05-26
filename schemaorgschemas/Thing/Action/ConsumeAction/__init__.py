# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ConsumeActionSchema(SchemaObject):

    """Schema Mixin for ConsumeAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of ingesting information/resources/food.
    """

    def __init__(self):
        self.schema = 'ConsumeAction'


class expectsAcceptanceOfProp(SchemaProperty):

    """
    SchemaField for expectsAcceptanceOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = expectsAcceptanceOfProp()  
    schema.org description:An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Offer"""

    _prop_schema = 'expectsAcceptanceOf'
    _expected_schema = 'Offer'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
