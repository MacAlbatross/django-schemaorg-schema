# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PhysicalExamSchema(SchemaObject):

    """Schema Mixin for PhysicalExam
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A type of physical examination of a patient performed by a physician. Enumerated type.
    """

    def __init__(self):
        self.schema = 'PhysicalExam'


/IDENTIFYINGEXAM_CHOICES = (
    ('/APPEARANCE', '/Appearance'),
    ('/CARDIOVASCULAREXAM', '/CardiovascularExam'),
    ('/EAR', '/Ear'),
    ('/EYE', '/Eye'),
    ('/GENITOURINARY', '/Genitourinary'),
    ('/HEAD', '/Head'),
    ('/LUNG', '/Lung'),
    ('/MUSCULOSKELETALEXAM', '/MusculoskeletalExam'),
    ('/NECK', '/Neck'),
    ('/NEURO', '/Neuro'),
    ('/NOSE', '/Nose'),
    ('/SKIN', '/Skin'),
    ('/THROAT', '/Throat'),
    ('/VITALSIGN', '/VitalSign'),
    ('/ABDOMEN', '/Abdomen'),
)


class / identifyingExamProp(SchemaEnumProperty):

    """
    Enumeration for /identifyingExam
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/identifyingExam'
    choices = /IDENTIFYINGEXAM_CHOICES
    _format_as = "enum"
    adapter = {
        '/APPEARANCE': '/Appearance',
        '/CARDIOVASCULAREXAM': '/CardiovascularExam',
        '/EAR': '/Ear',
        '/EYE': '/Eye',
        '/GENITOURINARY': '/Genitourinary',
        '/HEAD': '/Head',
        '/LUNG': '/Lung',
        '/MUSCULOSKELETALEXAM': '/MusculoskeletalExam',
        '/NECK': '/Neck',
        '/NEURO': '/Neuro',
        '/NOSE': '/Nose',
        '/SKIN': '/Skin',
        '/THROAT': '/Throat',
        '/VITALSIGN': '/VitalSign',
        '/ABDOMEN': '/Abdomen',
    }


# schema.org version 2.0
