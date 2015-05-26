# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PhysicalActivityCategorySchema(SchemaObject):

    """Schema Mixin for PhysicalActivityCategory
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Categories of physical activity, organized by physiologic classification.
    """

    def __init__(self):
        self.schema = 'PhysicalActivityCategory'


/CATEGORY_CHOICES = (
    ('/ANAEROBICACTIVITY', '/AnaerobicActivity'),
    ('/BALANCE', '/Balance'),
    ('/FLEXIBILITY', '/Flexibility'),
    ('/LEISURETIMEACTIVITY', '/LeisureTimeActivity'),
    ('/OCCUPATIONALACTIVITY', '/OccupationalActivity'),
    ('/STRENGTHTRAINING', '/StrengthTraining'),
    ('/AEROBICACTIVITY', '/AerobicActivity'),
)


class / categoryProp(SchemaEnumProperty):

    """
    Enumeration for /category
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/category'
    choices = /CATEGORY_CHOICES
    _format_as = "enum"
    adapter = {
        '/ANAEROBICACTIVITY': '/AnaerobicActivity',
        '/BALANCE': '/Balance',
        '/FLEXIBILITY': '/Flexibility',
        '/LEISURETIMEACTIVITY': '/LeisureTimeActivity',
        '/OCCUPATIONALACTIVITY': '/OccupationalActivity',
        '/STRENGTHTRAINING': '/StrengthTraining',
        '/AEROBICACTIVITY': '/AerobicActivity',
    }


# schema.org version 2.0
