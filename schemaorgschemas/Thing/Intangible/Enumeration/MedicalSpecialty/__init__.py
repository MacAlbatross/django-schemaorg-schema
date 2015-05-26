# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalSpecialtySchema(SchemaObject):

    """Schema Mixin for MedicalSpecialty
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalSpecialty'


/RELEVANTSPECIALTY_CHOICES = (
    ('/CARDIOVASCULAR', '/Cardiovascular'),
    ('/COMMUNITYHEALTH', '/CommunityHealth'),
    ('/DENTISTRY', '/Dentistry'),
    ('/DERMATOLOGIC', '/Dermatologic'),
    ('/DIETNUTRITION', '/DietNutrition'),
    ('/EMERGENCY', '/Emergency'),
    ('/ENDOCRINE', '/Endocrine'),
    ('/GASTROENTEROLOGIC', '/Gastroenterologic'),
    ('/GENETIC', '/Genetic'),
    ('/GERIATRIC', '/Geriatric'),
    ('/GYNECOLOGIC', '/Gynecologic'),
    ('/HEMATOLOGIC', '/Hematologic'),
    ('/INFECTIOUS', '/Infectious'),
    ('/LABORATORYSCIENCE', '/LaboratoryScience'),
    ('/MIDWIFERY', '/Midwifery'),
    ('/MUSCULOSKELETAL', '/Musculoskeletal'),
    ('/NEUROLOGIC', '/Neurologic'),
    ('/NURSING', '/Nursing'),
    ('/OBSTETRIC', '/Obstetric'),
    ('/OCCUPATIONALTHERAPY', '/OccupationalTherapy'),
    ('/ONCOLOGIC', '/Oncologic'),
    ('/OPTOMETIC', '/Optometic'),
    ('/OTOLARYNGOLOGIC', '/Otolaryngologic'),
    ('/PATHOLOGY', '/Pathology'),
    ('/PEDIATRIC', '/Pediatric'),
    ('/PHARMACYSPECIALTY', '/PharmacySpecialty'),
    ('/PHYSIOTHERAPY', '/Physiotherapy'),
    ('/PLASTICSURGERY', '/PlasticSurgery'),
    ('/PODIATRIC', '/Podiatric'),
    ('/PRIMARYCARE', '/PrimaryCare'),
    ('/PSYCHIATRIC', '/Psychiatric'),
    ('/PUBLICHEALTH', '/PublicHealth'),
    ('/PULMONARY', '/Pulmonary'),
    ('/RADIOGRAPY', '/Radiograpy'),
    ('/RENAL', '/Renal'),
    ('/RESPIRATORYTHERAPY', '/RespiratoryTherapy'),
    ('/RHEUMATOLOGIC', '/Rheumatologic'),
    ('/SPEECHPATHOLOGY', '/SpeechPathology'),
    ('/SURGICAL', '/Surgical'),
    ('/TOXICOLOGIC', '/Toxicologic'),
    ('/UROLOGIC', '/Urologic'),
    ('/ANESTHESIA', '/Anesthesia'),
)


class / relevantSpecialtyProp(SchemaEnumProperty):

    """
    Enumeration for /relevantSpecialty
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/relevantSpecialty'
    choices = /RELEVANTSPECIALTY_CHOICES
    _format_as = "enum"
    adapter = {
        '/CARDIOVASCULAR': '/Cardiovascular',
        '/COMMUNITYHEALTH': '/CommunityHealth',
        '/DENTISTRY': '/Dentistry',
        '/DERMATOLOGIC': '/Dermatologic',
        '/DIETNUTRITION': '/DietNutrition',
        '/EMERGENCY': '/Emergency',
        '/ENDOCRINE': '/Endocrine',
        '/GASTROENTEROLOGIC': '/Gastroenterologic',
        '/GENETIC': '/Genetic',
        '/GERIATRIC': '/Geriatric',
        '/GYNECOLOGIC': '/Gynecologic',
        '/HEMATOLOGIC': '/Hematologic',
        '/INFECTIOUS': '/Infectious',
        '/LABORATORYSCIENCE': '/LaboratoryScience',
        '/MIDWIFERY': '/Midwifery',
        '/MUSCULOSKELETAL': '/Musculoskeletal',
        '/NEUROLOGIC': '/Neurologic',
        '/NURSING': '/Nursing',
        '/OBSTETRIC': '/Obstetric',
        '/OCCUPATIONALTHERAPY': '/OccupationalTherapy',
        '/ONCOLOGIC': '/Oncologic',
        '/OPTOMETIC': '/Optometic',
        '/OTOLARYNGOLOGIC': '/Otolaryngologic',
        '/PATHOLOGY': '/Pathology',
        '/PEDIATRIC': '/Pediatric',
        '/PHARMACYSPECIALTY': '/PharmacySpecialty',
        '/PHYSIOTHERAPY': '/Physiotherapy',
        '/PLASTICSURGERY': '/PlasticSurgery',
        '/PODIATRIC': '/Podiatric',
        '/PRIMARYCARE': '/PrimaryCare',
        '/PSYCHIATRIC': '/Psychiatric',
        '/PUBLICHEALTH': '/PublicHealth',
        '/PULMONARY': '/Pulmonary',
        '/RADIOGRAPY': '/Radiograpy',
        '/RENAL': '/Renal',
        '/RESPIRATORYTHERAPY': '/RespiratoryTherapy',
        '/RHEUMATOLOGIC': '/Rheumatologic',
        '/SPEECHPATHOLOGY': '/SpeechPathology',
        '/SURGICAL': '/Surgical',
        '/TOXICOLOGIC': '/Toxicologic',
        '/UROLOGIC': '/Urologic',
        '/ANESTHESIA': '/Anesthesia',
    }


/MEDICALSPECIALTY_CHOICES = (
    ('/CARDIOVASCULAR', '/Cardiovascular'),
    ('/COMMUNITYHEALTH', '/CommunityHealth'),
    ('/DENTISTRY', '/Dentistry'),
    ('/DERMATOLOGIC', '/Dermatologic'),
    ('/DIETNUTRITION', '/DietNutrition'),
    ('/EMERGENCY', '/Emergency'),
    ('/ENDOCRINE', '/Endocrine'),
    ('/GASTROENTEROLOGIC', '/Gastroenterologic'),
    ('/GENETIC', '/Genetic'),
    ('/GERIATRIC', '/Geriatric'),
    ('/GYNECOLOGIC', '/Gynecologic'),
    ('/HEMATOLOGIC', '/Hematologic'),
    ('/INFECTIOUS', '/Infectious'),
    ('/LABORATORYSCIENCE', '/LaboratoryScience'),
    ('/MIDWIFERY', '/Midwifery'),
    ('/MUSCULOSKELETAL', '/Musculoskeletal'),
    ('/NEUROLOGIC', '/Neurologic'),
    ('/NURSING', '/Nursing'),
    ('/OBSTETRIC', '/Obstetric'),
    ('/OCCUPATIONALTHERAPY', '/OccupationalTherapy'),
    ('/ONCOLOGIC', '/Oncologic'),
    ('/OPTOMETIC', '/Optometic'),
    ('/OTOLARYNGOLOGIC', '/Otolaryngologic'),
    ('/PATHOLOGY', '/Pathology'),
    ('/PEDIATRIC', '/Pediatric'),
    ('/PHARMACYSPECIALTY', '/PharmacySpecialty'),
    ('/PHYSIOTHERAPY', '/Physiotherapy'),
    ('/PLASTICSURGERY', '/PlasticSurgery'),
    ('/PODIATRIC', '/Podiatric'),
    ('/PRIMARYCARE', '/PrimaryCare'),
    ('/PSYCHIATRIC', '/Psychiatric'),
    ('/PUBLICHEALTH', '/PublicHealth'),
    ('/PULMONARY', '/Pulmonary'),
    ('/RADIOGRAPY', '/Radiograpy'),
    ('/RENAL', '/Renal'),
    ('/RESPIRATORYTHERAPY', '/RespiratoryTherapy'),
    ('/RHEUMATOLOGIC', '/Rheumatologic'),
    ('/SPEECHPATHOLOGY', '/SpeechPathology'),
    ('/SURGICAL', '/Surgical'),
    ('/TOXICOLOGIC', '/Toxicologic'),
    ('/UROLOGIC', '/Urologic'),
    ('/ANESTHESIA', '/Anesthesia'),
)


class / medicalSpecialtyProp(SchemaEnumProperty):

    """
    Enumeration for /medicalSpecialty
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/medicalSpecialty'
    choices = /MEDICALSPECIALTY_CHOICES
    _format_as = "enum"
    adapter = {
        '/CARDIOVASCULAR': '/Cardiovascular',
        '/COMMUNITYHEALTH': '/CommunityHealth',
        '/DENTISTRY': '/Dentistry',
        '/DERMATOLOGIC': '/Dermatologic',
        '/DIETNUTRITION': '/DietNutrition',
        '/EMERGENCY': '/Emergency',
        '/ENDOCRINE': '/Endocrine',
        '/GASTROENTEROLOGIC': '/Gastroenterologic',
        '/GENETIC': '/Genetic',
        '/GERIATRIC': '/Geriatric',
        '/GYNECOLOGIC': '/Gynecologic',
        '/HEMATOLOGIC': '/Hematologic',
        '/INFECTIOUS': '/Infectious',
        '/LABORATORYSCIENCE': '/LaboratoryScience',
        '/MIDWIFERY': '/Midwifery',
        '/MUSCULOSKELETAL': '/Musculoskeletal',
        '/NEUROLOGIC': '/Neurologic',
        '/NURSING': '/Nursing',
        '/OBSTETRIC': '/Obstetric',
        '/OCCUPATIONALTHERAPY': '/OccupationalTherapy',
        '/ONCOLOGIC': '/Oncologic',
        '/OPTOMETIC': '/Optometic',
        '/OTOLARYNGOLOGIC': '/Otolaryngologic',
        '/PATHOLOGY': '/Pathology',
        '/PEDIATRIC': '/Pediatric',
        '/PHARMACYSPECIALTY': '/PharmacySpecialty',
        '/PHYSIOTHERAPY': '/Physiotherapy',
        '/PLASTICSURGERY': '/PlasticSurgery',
        '/PODIATRIC': '/Podiatric',
        '/PRIMARYCARE': '/PrimaryCare',
        '/PSYCHIATRIC': '/Psychiatric',
        '/PUBLICHEALTH': '/PublicHealth',
        '/PULMONARY': '/Pulmonary',
        '/RADIOGRAPY': '/Radiograpy',
        '/RENAL': '/Renal',
        '/RESPIRATORYTHERAPY': '/RespiratoryTherapy',
        '/RHEUMATOLOGIC': '/Rheumatologic',
        '/SPEECHPATHOLOGY': '/SpeechPathology',
        '/SURGICAL': '/Surgical',
        '/TOXICOLOGIC': '/Toxicologic',
        '/UROLOGIC': '/Urologic',
        '/ANESTHESIA': '/Anesthesia',
    }


# schema.org version 2.0
