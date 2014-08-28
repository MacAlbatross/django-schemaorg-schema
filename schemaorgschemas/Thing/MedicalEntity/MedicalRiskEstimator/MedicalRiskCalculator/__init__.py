# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalRiskEstimator import estimatesRiskOfProp, includedRiskFactorProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalRiskCalculatorSchema(SchemaObject):

    """Schema Mixin for MedicalRiskCalculator
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A complex mathematical calculation requiring an online calculator, used to assess prognosis. Note: use the url property of Thing to record any URLs for online calculators.
    """

    def __init__(self):
        self.schema = 'MedicalRiskCalculator'
