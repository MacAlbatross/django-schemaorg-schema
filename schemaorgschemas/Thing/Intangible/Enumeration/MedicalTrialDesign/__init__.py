# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalTrialDesignSchema(SchemaObject):

    """Schema Mixin for MedicalTrialDesign
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Design models for medical trials. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalTrialDesign'


TRIALDESIGN_CHOICES = (
    ('INTERNATIONALTRIAL', 'InternationalTrial: An international trial.'),
    ('MULTICENTERTRIAL',
     'MultiCenterTrial: A trial that takes place at multiple centers.'),
    ('OPENTRIAL',
     'OpenTrial: A trial design in which the researcher knows the full details of the treatment, and so does the patient.'),
    ('PLACEBOCONTROLLEDTRIAL',
     'PlaceboControlledTrial: A placebo-controlled trial design.'),
    ('RANDOMIZEDTRIAL', 'RandomizedTrial: A randomized trial design.'),
    ('SINGLEBLINDEDTRIAL',
     'SingleBlindedTrial: A trial design in which the researcher knows which treatment the patient was randomly assigned to but the patient does not.'),
    ('SINGLECENTERTRIAL',
     'SingleCenterTrial: A trial that takes place at a single center.'),
    ('TRIPLEBLINDEDTRIAL',
     'TripleBlindedTrial: A trial design in which neither the researcher, the person administering the therapy nor the patient knows the details of the treatment the patient was randomly assigned to.'),
    ('DOUBLEBLINDEDTRIAL',
     'DoubleBlindedTrial: A trial design in which neither the researcher nor the patient knows the details of the treatment the patient was randomly assigned to.'),
)


class trialDesignProp(SchemaEnumProperty):

    """
    Enumeration for trialDesign
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'trialDesign'
    choices = TRIALDESIGN_CHOICES
    _format_as = "enum"
    adapter = {
        'INTERNATIONALTRIAL': 'InternationalTrial',
        'MULTICENTERTRIAL': 'MultiCenterTrial',
        'OPENTRIAL': 'OpenTrial',
        'PLACEBOCONTROLLEDTRIAL': 'PlaceboControlledTrial',
        'RANDOMIZEDTRIAL': 'RandomizedTrial',
        'SINGLEBLINDEDTRIAL': 'SingleBlindedTrial',
        'SINGLECENTERTRIAL': 'SingleCenterTrial',
        'TRIPLEBLINDEDTRIAL': 'TripleBlindedTrial',
        'DOUBLEBLINDEDTRIAL': 'DoubleBlindedTrial',
    }


# schema.org version 2.0
