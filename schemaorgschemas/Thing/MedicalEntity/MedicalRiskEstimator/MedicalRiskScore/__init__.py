# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalRiskEstimator import estimatesRiskOfProp, includedRiskFactorProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalRiskScoreSchema(SchemaObject):

    """Schema Mixin for MedicalRiskScore
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A simple system that adds up the number of risk factors to yield a score that is associated with prognosis, e.g. CHAD score, TIMI risk score.
    """

    def __init__(self):
        self.schema = 'MedicalRiskScore'


class algorithmProp(SchemaProperty):

    """
    SchemaField for algorithm
    Usage: Include in SchemaObject SchemaFields as your_django_field = algorithmProp()
    schema.org description:The algorithm or rules to follow to compute the score.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'algorithm'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
