# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalConditionStageSchema(SchemaObject):

    """Schema Mixin for MedicalConditionStage
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A stage of a medical condition, such as &#39;Stage IIIa&#39;.
    """

    def __init__(self):
        self.schema = 'MedicalConditionStage'


class stageAsNumberProp(SchemaProperty):

    """
    SchemaField for stageAsNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = stageAsNumberProp()  
    schema.org description:The stage represented as a number, e.g. 3.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'stageAsNumber'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class subStageSuffixProp(SchemaProperty):

    """
    SchemaField for subStageSuffix
    Usage: Include in SchemaObject SchemaFields as your_django_field = subStageSuffixProp()  
    schema.org description:The substage, e.g. &#39;a&#39; for Stage IIIa.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'subStageSuffix'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
