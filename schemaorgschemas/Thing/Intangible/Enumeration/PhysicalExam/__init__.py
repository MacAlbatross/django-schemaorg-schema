# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PhysicalExamSchema(SchemaObject):

    """Schema Mixin for PhysicalExam
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A type of physical examination of a patient performed by a physician. Enumerated type.
    """

    def __init__(self):
        self.schema = 'PhysicalExam'


IDENTIFYINGEXAM_CHOICES = (
    ('APPEARANCE', 'Appearance: Appearance'),
    ('CARDIOVASCULAREXAM', 'CardiovascularExam: Cardiovascular'),
    ('EAR', 'Ear: Ear'),
    ('EYE', 'Eye: Eye'),
    ('GENITOURINARY', 'Genitourinary: Genitourinary'),
    ('HEAD', 'Head: Head'),
    ('LUNG', 'Lung: Lung'),
    ('MUSCULOSKELETALEXAM', 'MusculoskeletalExam: Musculoskeletal'),
    ('NECK', 'Neck: Neck'),
    ('NEURO', 'Neuro: Neuro'),
    ('NOSE', 'Nose: Nose'),
    ('SKIN', 'Skin: Skin'),
    ('THROAT', 'Throat: Throat'),
    ('VITALSIGN', 'VitalSign: VitalSign'),
    ('ABDOMEN', 'Abdomen: Abdomen'),
)


class identifyingExamProp(SchemaEnumProperty):

    """
    Enumeration for identifyingExam
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'identifyingExam'
    choices = IDENTIFYINGEXAM_CHOICES
    _format_as = "enum"
    adapter = {
        'APPEARANCE': 'Appearance',
        'CARDIOVASCULAREXAM': 'CardiovascularExam',
        'EAR': 'Ear',
        'EYE': 'Eye',
        'GENITOURINARY': 'Genitourinary',
        'HEAD': 'Head',
        'LUNG': 'Lung',
        'MUSCULOSKELETALEXAM': 'MusculoskeletalExam',
        'NECK': 'Neck',
        'NEURO': 'Neuro',
        'NOSE': 'Nose',
        'SKIN': 'Skin',
        'THROAT': 'Throat',
        'VITALSIGN': 'VitalSign',
        'ABDOMEN': 'Abdomen',
    }
