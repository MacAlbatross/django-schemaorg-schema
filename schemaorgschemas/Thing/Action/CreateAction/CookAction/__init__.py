# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CookActionSchema(SchemaObject):

    """Schema Mixin for CookAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of producing/preparing food.
    """

    def __init__(self):
        self.schema = 'CookAction'


class recipeProp(SchemaProperty):

    """
    SchemaField for recipe
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipeProp()  
    schema.org description:A sub property of instrument. The recipe/instructions used to perform the action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Recipe"""

    _prop_schema = 'recipe'
    _expected_schema = 'Recipe'
    _enum = False
    _format_as = "ForeignKey"


class foodEstablishmentProp(SchemaProperty):

    """
    SchemaField for foodEstablishment
    Usage: Include in SchemaObject SchemaFields as your_django_field = foodEstablishmentProp()  
    schema.org description:A sub property of location. The specific food establishment where the action occurred.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference FoodEstablishment"""

    _prop_schema = 'foodEstablishment'
    _expected_schema = 'FoodEstablishment'
    _enum = False
    _format_as = "ForeignKey"


class foodEventProp(SchemaProperty):

    """
    SchemaField for foodEvent
    Usage: Include in SchemaObject SchemaFields as your_django_field = foodEventProp()  
    schema.org description:A sub property of location. The specific food event where the action occurred.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference FoodEvent"""

    _prop_schema = 'foodEvent'
    _expected_schema = 'FoodEvent'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
