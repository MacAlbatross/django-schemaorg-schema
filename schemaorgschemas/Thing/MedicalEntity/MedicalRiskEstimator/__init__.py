# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalRiskEstimatorSchema(SchemaObject):

    """Schema Mixin for MedicalRiskEstimator
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any rule set or interactive tool for estimating the risk of developing a complication or condition.
    """

    def __init__(self):
        self.schema = 'MedicalRiskEstimator'


class estimatesRiskOfProp(SchemaProperty):

    """
    SchemaField for estimatesRiskOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = estimatesRiskOfProp()  
    schema.org description:The condition, complication, or symptom whose risk is being estimated.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalEntity"""

    _prop_schema = 'estimatesRiskOf'
    _expected_schema = 'MedicalEntity'
    _enum = False
    _format_as = "ForeignKey"


class includedRiskFactorProp(SchemaProperty):

    """
    SchemaField for includedRiskFactor
    Usage: Include in SchemaObject SchemaFields as your_django_field = includedRiskFactorProp()  
    schema.org description:A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalRiskFactor"""

    _prop_schema = 'includedRiskFactor'
    _expected_schema = 'MedicalRiskFactor'
    _enum = False
    _format_as = "ForeignKey"
