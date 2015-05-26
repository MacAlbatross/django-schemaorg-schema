# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Enumeration.QualitativeValue import valueReferenceProp, greaterProp, lesserOrEqualProp, equalProp, lesserProp, additionalPropertyProp, greaterOrEqualProp, nonEqualProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SteeringPositionValueSchema(SchemaObject):

    """Schema Mixin for SteeringPositionValue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A value indicating a steering position.
    """

    def __init__(self):
        self.schema = 'SteeringPositionValue'


STEERINGPOSITION_CHOICES = (
    ('RIGHTHANDDRIVING',
     'RightHandDriving: The steering position is on the right side of the vehicle (viewed from the main direction of driving).'),
    ('LEFTHANDDRIVING',
     'LeftHandDriving: The steering position is on the left side of the vehicle (viewed from the main direction of driving).'),
)


class steeringPositionProp(SchemaEnumProperty):

    """
    Enumeration for steeringPosition
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'steeringPosition'
    choices = STEERINGPOSITION_CHOICES
    _format_as = "enum"
    adapter = {
        'RIGHTHANDDRIVING': 'RightHandDriving',
        'LEFTHANDDRIVING': 'LeftHandDriving',
    }


# schema.org version 2.0
