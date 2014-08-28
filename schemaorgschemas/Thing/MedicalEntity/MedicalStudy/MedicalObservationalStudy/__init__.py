# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalStudy import statusProp, studySubjectProp, sponsorProp, studyLocationProp, outcomeProp, populationProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalObservationalStudySchema(SchemaObject):

    """Schema Mixin for MedicalObservationalStudy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An observational study is a type of medical study that attempts to infer the possible effect of a treatment through observation of a cohort of subjects over a period of time. In an observational study, the assignment of subjects into treatment groups versus control groups is outside the control of the investigator. This is in contrast with controlled studies, such as the randomized controlled trials represented by MedicalTrial, where each subject is randomly assigned to a treatment group or a control group before the start of the treatment.
    """

    def __init__(self):
        self.schema = 'MedicalObservationalStudy'


class studyDesignProp(SchemaProperty):

    """
    SchemaField for studyDesign
    Usage: Include in SchemaObject SchemaFields as your_django_field = studyDesignProp()  
    schema.org description:Specifics about the observational study design (enumerated).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalObservationalStudyDesign"""

    _prop_schema = 'studyDesign'
    _expected_schema = 'MedicalObservationalStudyDesign'
    _enum = False
    _format_as = "ForeignKey"
