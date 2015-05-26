# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.MedicalEntity.MedicalSignOrSymptom import possibleTreatmentProp, causeProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalSignSchema(SchemaObject):

    """Schema Mixin for MedicalSign
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any physical manifestation of a person&#39;s medical condition discoverable by objective diagnostic tests or physical examination.
    """

    def __init__(self):
        self.schema = 'MedicalSign'


class identifyingExamProp(SchemaProperty):

    """
    SchemaField for identifyingExam
    Usage: Include in SchemaObject SchemaFields as your_django_field = identifyingExamProp()  
    schema.org description:A physical examination that can identify this sign.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PhysicalExam"""

    _prop_schema = 'identifyingExam'
    _expected_schema = 'PhysicalExam'
    _enum = False
    _format_as = "ForeignKey"


class identifyingTestProp(SchemaProperty):

    """
    SchemaField for identifyingTest
    Usage: Include in SchemaObject SchemaFields as your_django_field = identifyingTestProp()  
    schema.org description:A diagnostic test that can identify this sign.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTest"""

    _prop_schema = 'identifyingTest'
    _expected_schema = 'MedicalTest'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
