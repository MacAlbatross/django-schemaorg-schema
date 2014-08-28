# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalGuideline import evidenceLevelProp, evidenceOriginProp, guidelineSubjectProp, guidelineDateProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalGuidelineRecommendationSchema(SchemaObject):

    """Schema Mixin for MedicalGuidelineRecommendation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A guideline recommendation that is regarded as efficacious and where quality of the data supporting the recommendation is sound.
    """

    def __init__(self):
        self.schema = 'MedicalGuidelineRecommendation'


class recommendationStrengthProp(SchemaProperty):

    """
    SchemaField for recommendationStrength
    Usage: Include in SchemaObject SchemaFields as your_django_field = recommendationStrengthProp()  
    schema.org description:Strength of the guideline&#39;s recommendation (e.g. &#39;class I&#39;).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'recommendationStrength'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
