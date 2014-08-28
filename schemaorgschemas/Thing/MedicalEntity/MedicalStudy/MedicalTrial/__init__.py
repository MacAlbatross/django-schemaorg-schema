# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalStudy import statusProp, studySubjectProp, sponsorProp, studyLocationProp, outcomeProp, populationProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalTrialSchema(SchemaObject):

    """Schema Mixin for MedicalTrial
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A medical trial is a type of medical study that uses scientific process used to compare the safety and efficacy of medical therapies or medical procedures. In general, medical trials are controlled and subjects are allocated at random to the different treatment and/or control groups.
    """

    def __init__(self):
        self.schema = 'MedicalTrial'


class phaseProp(SchemaProperty):

    """
    SchemaField for phase
    Usage: Include in SchemaObject SchemaFields as your_django_field = phaseProp()
    schema.org description:The phase of the trial.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'phase'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class trialDesignProp(SchemaProperty):

    """
    SchemaField for trialDesign
    Usage: Include in SchemaObject SchemaFields as your_django_field = trialDesignProp()
    schema.org description:Specifics about the trial design (enumerated).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTrialDesign"""

    _prop_schema = 'trialDesign'
    _expected_schema = 'MedicalTrialDesign'
    _enum = False
    _format_as = "ForeignKey"
