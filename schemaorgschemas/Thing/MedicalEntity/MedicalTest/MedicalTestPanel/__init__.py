# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTest import affectedByProp, usedToDiagnoseProp, normalRangeProp, usesDeviceProp, signDetectedProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalTestPanelSchema(SchemaObject):

    """Schema Mixin for MedicalTestPanel
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any collection of tests commonly ordered together.
    """

    def __init__(self):
        self.schema = 'MedicalTestPanel'


class subTestProp(SchemaProperty):

    """
    SchemaField for subTest
    Usage: Include in SchemaObject SchemaFields as your_django_field = subTestProp()  
    schema.org description:A component test of the panel.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTest"""

    _prop_schema = 'subTest'
    _expected_schema = 'MedicalTest'
    _enum = False
    _format_as = "ForeignKey"
