# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OfferItemConditionSchema(SchemaObject):

    """Schema Mixin for OfferItemCondition
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A list of possible conditions for the item.
    """

    def __init__(self):
        self.schema = 'OfferItemCondition'


/ITEMCONDITION_CHOICES = (
    ('/NEWCONDITION', '/NewCondition'),
    ('/REFURBISHEDCONDITION', '/RefurbishedCondition'),
    ('/USEDCONDITION', '/UsedCondition'),
    ('/DAMAGEDCONDITION', '/DamagedCondition'),
)


class / itemConditionProp(SchemaEnumProperty):

    """
    Enumeration for /itemCondition
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/itemCondition'
    choices = /ITEMCONDITION_CHOICES
    _format_as = "enum"
    adapter = {
        '/NEWCONDITION': '/NewCondition',
        '/REFURBISHEDCONDITION': '/RefurbishedCondition',
        '/USEDCONDITION': '/UsedCondition',
        '/DAMAGEDCONDITION': '/DamagedCondition',
    }


# schema.org version 2.0
