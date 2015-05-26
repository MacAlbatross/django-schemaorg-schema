# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BoardingPolicyTypeSchema(SchemaObject):

    """Schema Mixin for BoardingPolicyType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A type of boarding policy used by an airline.
    """

    def __init__(self):
        self.schema = 'BoardingPolicyType'


/BOARDINGPOLICY_CHOICES = (
    ('/ZONEBOARDINGPOLICY', '/ZoneBoardingPolicy'),
    ('/GROUPBOARDINGPOLICY', '/GroupBoardingPolicy'),
)


class / boardingPolicyProp(SchemaEnumProperty):

    """
    Enumeration for /boardingPolicy
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/boardingPolicy'
    choices = /BOARDINGPOLICY_CHOICES
    _format_as = "enum"
    adapter = {
        '/ZONEBOARDINGPOLICY': '/ZoneBoardingPolicy',
        '/GROUPBOARDINGPOLICY': '/GroupBoardingPolicy',
    }


# schema.org version 2.0
