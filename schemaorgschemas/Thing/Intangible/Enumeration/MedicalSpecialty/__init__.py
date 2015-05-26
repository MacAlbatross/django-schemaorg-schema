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


MEDICALSPECIALTY_CHOICES = (
    ('CARDIOVASCULAR',
     'Cardiovascular: A specific branch of medical science that pertains to diagnosis and treatment of disorders of heart and vasculature.'),
    ('COMMUNITYHEALTH', 'CommunityHealth: Community health.'),
    ('DENTISTRY', 'Dentistry: Dentistry.'),
    ('DERMATOLOGIC',
     'Dermatologic: A specific branch of medical science that pertains to diagnosis and treatment of disorders of skin.'),
    ('DIETNUTRITION', 'DietNutrition: Diet and nutrition.'),
    ('EMERGENCY',
     'Emergency: A specific branch of medical science that is deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.'),
    ('ENDOCRINE',
     'Endocrine: A specific branch of medical science that pertains to diagnosis and treatment of disorders of endocrine glands and their secretions.'),
    ('GASTROENTEROLOGIC',
     'Gastroenterologic: A specific branch of medical science that pertains to diagnosis and treatment of disorders of digestive system.'),
    ('GENETIC',
     'Genetic: A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders.'),
    ('GERIATRIC',
     'Geriatric: A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.'),
    ('HEMATOLOGIC',
     'Hematologic: A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.'),
    ('INFECTIOUS',
     'Infectious: A specific branch of medical science that pertains to diagnosis and treatment of bacterial, viral, fungal and parasitic infections.'),
    ('LABORATORYSCIENCE', 'LaboratoryScience: Laboratory science.'),
    ('MIDWIFERY', 'Midwifery: Midwifery.'),
    ('MUSCULOSKELETAL',
     'Musculoskeletal: A specific branch of medical science that pertains to diagnosis and treatment of disorders of muscles, ligaments and skeletal system.'),
    ('NEUROLOGIC',
     'Neurologic: A specific branch of medical science that studies the nerves and nervous system and its respective disease states.'),
    ('NURSING', 'Nursing: Nursing.'),
    ('OBSTETRIC',
     'Obstetric: A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child.'),
    ('OCCUPATIONALTHERAPY', 'OccupationalTherapy: Occupational therapy.'),
    ('ONCOLOGIC',
     'Oncologic: A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention.'),
    ('OPTOMETIC', 'Optometic: Optometry.'),
    ('OTOLARYNGOLOGIC',
     'Otolaryngologic: A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states.'),
    ('PATHOLOGY',
     'Pathology: A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.'),
    ('PEDIATRIC',
     'Pediatric: A specific branch of medical science that specializes in the care of infants, children and adolescents.'),
    ('PHARMACYSPECIALTY', 'PharmacySpecialty: Pharmacy.'),
    ('PHYSIOTHERAPY', 'Physiotherapy: Physiotherapy.'),
    ('PLASTICSURGERY',
     'PlasticSurgery: A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means.'),
    ('PODIATRIC', 'Podiatric: Podiatry.'),
    ('PSYCHIATRIC',
     'Psychiatric: A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.'),
    ('PUBLICHEALTH', 'PublicHealth: Environment and public health.'),
    ('PULMONARY',
     'Pulmonary: A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states.'),
    ('RADIOGRAPY', 'Radiograpy: Radiography.'),
    ('RENAL',
     'Renal: A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.'),
    ('RESPIRATORYTHERAPY', 'RespiratoryTherapy: Respiratory therapy.'),
    ('RHEUMATOLOGIC',
     'Rheumatologic: A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases.'),
    ('SPEECHPATHOLOGY', 'SpeechPathology: Speech pathology.'),
    ('SURGICAL',
     'Surgical: A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.'),
    ('TOXICOLOGIC',
     'Toxicologic: A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning.'),
    ('UROLOGIC',
     'Urologic: A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining to the urinary tract and the urogenital system.'),
    ('ANESTHESIA',
     'Anesthesia: A specific branch of medical science that pertains to study of anesthetics and their application.'),
    ('GYNECOLOGIC',
     'Gynecologic: A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system.'),
    ('PRIMARYCARE', 'PrimaryCare: Primary care.'),
)


class medicalSpecialtyProp(SchemaEnumProperty):

    """
    Enumeration for medicalSpecialty
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'medicalSpecialty'
    choices = MEDICALSPECIALTY_CHOICES
    _format_as = "enum"
    adapter = {
        'CARDIOVASCULAR': 'Cardiovascular',
        'COMMUNITYHEALTH': 'CommunityHealth',
        'DENTISTRY': 'Dentistry',
        'DERMATOLOGIC': 'Dermatologic',
        'DIETNUTRITION': 'DietNutrition',
        'EMERGENCY': 'Emergency',
        'ENDOCRINE': 'Endocrine',
        'GASTROENTEROLOGIC': 'Gastroenterologic',
        'GENETIC': 'Genetic',
        'GERIATRIC': 'Geriatric',
        'HEMATOLOGIC': 'Hematologic',
        'INFECTIOUS': 'Infectious',
        'LABORATORYSCIENCE': 'LaboratoryScience',
        'MIDWIFERY': 'Midwifery',
        'MUSCULOSKELETAL': 'Musculoskeletal',
        'NEUROLOGIC': 'Neurologic',
        'NURSING': 'Nursing',
        'OBSTETRIC': 'Obstetric',
        'OCCUPATIONALTHERAPY': 'OccupationalTherapy',
        'ONCOLOGIC': 'Oncologic',
        'OPTOMETIC': 'Optometic',
        'OTOLARYNGOLOGIC': 'Otolaryngologic',
        'PATHOLOGY': 'Pathology',
        'PEDIATRIC': 'Pediatric',
        'PHARMACYSPECIALTY': 'PharmacySpecialty',
        'PHYSIOTHERAPY': 'Physiotherapy',
        'PLASTICSURGERY': 'PlasticSurgery',
        'PODIATRIC': 'Podiatric',
        'PSYCHIATRIC': 'Psychiatric',
        'PUBLICHEALTH': 'PublicHealth',
        'PULMONARY': 'Pulmonary',
        'RADIOGRAPY': 'Radiograpy',
        'RENAL': 'Renal',
        'RESPIRATORYTHERAPY': 'RespiratoryTherapy',
        'RHEUMATOLOGIC': 'Rheumatologic',
        'SPEECHPATHOLOGY': 'SpeechPathology',
        'SURGICAL': 'Surgical',
        'TOXICOLOGIC': 'Toxicologic',
        'UROLOGIC': 'Urologic',
        'ANESTHESIA': 'Anesthesia',
        'GYNECOLOGIC': 'Gynecologic',
        'PRIMARYCARE': 'PrimaryCare',
    }


RELEVANTSPECIALTY_CHOICES = (
    ('CARDIOVASCULAR',
     'Cardiovascular: A specific branch of medical science that pertains to diagnosis and treatment of disorders of heart and vasculature.'),
    ('COMMUNITYHEALTH', 'CommunityHealth: Community health.'),
    ('DENTISTRY', 'Dentistry: Dentistry.'),
    ('DERMATOLOGIC',
     'Dermatologic: A specific branch of medical science that pertains to diagnosis and treatment of disorders of skin.'),
    ('DIETNUTRITION', 'DietNutrition: Diet and nutrition.'),
    ('EMERGENCY',
     'Emergency: A specific branch of medical science that is deals with the evaluation and initial treatment of medical conditions caused by trauma or sudden illness.'),
    ('ENDOCRINE',
     'Endocrine: A specific branch of medical science that pertains to diagnosis and treatment of disorders of endocrine glands and their secretions.'),
    ('GASTROENTEROLOGIC',
     'Gastroenterologic: A specific branch of medical science that pertains to diagnosis and treatment of disorders of digestive system.'),
    ('GENETIC',
     'Genetic: A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders.'),
    ('GERIATRIC',
     'Geriatric: A specific branch of medical science that is concerned with the diagnosis and treatment of diseases, debilities and provision of care to the aged.'),
    ('HEMATOLOGIC',
     'Hematologic: A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.'),
    ('INFECTIOUS',
     'Infectious: A specific branch of medical science that pertains to diagnosis and treatment of bacterial, viral, fungal and parasitic infections.'),
    ('LABORATORYSCIENCE', 'LaboratoryScience: Laboratory science.'),
    ('MIDWIFERY', 'Midwifery: Midwifery.'),
    ('MUSCULOSKELETAL',
     'Musculoskeletal: A specific branch of medical science that pertains to diagnosis and treatment of disorders of muscles, ligaments and skeletal system.'),
    ('NEUROLOGIC',
     'Neurologic: A specific branch of medical science that studies the nerves and nervous system and its respective disease states.'),
    ('NURSING', 'Nursing: Nursing.'),
    ('OBSTETRIC',
     'Obstetric: A specific branch of medical science that specializes in the care of women during the prenatal and postnatal care and with the delivery of the child.'),
    ('OCCUPATIONALTHERAPY', 'OccupationalTherapy: Occupational therapy.'),
    ('ONCOLOGIC',
     'Oncologic: A specific branch of medical science that deals with benign and malignant tumors, including the study of their development, diagnosis, treatment and prevention.'),
    ('OPTOMETIC', 'Optometic: Optometry.'),
    ('OTOLARYNGOLOGIC',
     'Otolaryngologic: A specific branch of medical science that is concerned with the ear, nose and throat and their respective disease states.'),
    ('PATHOLOGY',
     'Pathology: A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.'),
    ('PEDIATRIC',
     'Pediatric: A specific branch of medical science that specializes in the care of infants, children and adolescents.'),
    ('PHARMACYSPECIALTY', 'PharmacySpecialty: Pharmacy.'),
    ('PHYSIOTHERAPY', 'Physiotherapy: Physiotherapy.'),
    ('PLASTICSURGERY',
     'PlasticSurgery: A specific branch of medical science that pertains to therapeutic or cosmetic repair or re-formation of missing, injured or malformed tissues or body parts by manual and instrumental means.'),
    ('PODIATRIC', 'Podiatric: Podiatry.'),
    ('PSYCHIATRIC',
     'Psychiatric: A specific branch of medical science that is concerned with the study, treatment, and prevention of mental illness, using both medical and psychological therapies.'),
    ('PUBLICHEALTH', 'PublicHealth: Environment and public health.'),
    ('PULMONARY',
     'Pulmonary: A specific branch of medical science that pertains to the study of the respiratory system and its respective disease states.'),
    ('RADIOGRAPY', 'Radiograpy: Radiography.'),
    ('RENAL',
     'Renal: A specific branch of medical science that pertains to the study of the kidneys and its respective disease states.'),
    ('RESPIRATORYTHERAPY', 'RespiratoryTherapy: Respiratory therapy.'),
    ('RHEUMATOLOGIC',
     'Rheumatologic: A specific branch of medical science that deals with the study and treatment of rheumatic, autoimmune or joint diseases.'),
    ('SPEECHPATHOLOGY', 'SpeechPathology: Speech pathology.'),
    ('SURGICAL',
     'Surgical: A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.'),
    ('TOXICOLOGIC',
     'Toxicologic: A specific branch of medical science that is concerned with poisons, their nature, effects and detection and involved in the treatment of poisoning.'),
    ('UROLOGIC',
     'Urologic: A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining to the urinary tract and the urogenital system.'),
    ('ANESTHESIA',
     'Anesthesia: A specific branch of medical science that pertains to study of anesthetics and their application.'),
    ('GYNECOLOGIC',
     'Gynecologic: A specific branch of medical science that pertains to the health care of women, particularly in the diagnosis and treatment of disorders affecting the female reproductive system.'),
    ('PRIMARYCARE', 'PrimaryCare: Primary care.'),
)


class relevantSpecialtyProp(SchemaEnumProperty):

    """
    Enumeration for relevantSpecialty
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'relevantSpecialty'
    choices = RELEVANTSPECIALTY_CHOICES
    _format_as = "enum"
    adapter = {
        'CARDIOVASCULAR': 'Cardiovascular',
        'COMMUNITYHEALTH': 'CommunityHealth',
        'DENTISTRY': 'Dentistry',
        'DERMATOLOGIC': 'Dermatologic',
        'DIETNUTRITION': 'DietNutrition',
        'EMERGENCY': 'Emergency',
        'ENDOCRINE': 'Endocrine',
        'GASTROENTEROLOGIC': 'Gastroenterologic',
        'GENETIC': 'Genetic',
        'GERIATRIC': 'Geriatric',
        'HEMATOLOGIC': 'Hematologic',
        'INFECTIOUS': 'Infectious',
        'LABORATORYSCIENCE': 'LaboratoryScience',
        'MIDWIFERY': 'Midwifery',
        'MUSCULOSKELETAL': 'Musculoskeletal',
        'NEUROLOGIC': 'Neurologic',
        'NURSING': 'Nursing',
        'OBSTETRIC': 'Obstetric',
        'OCCUPATIONALTHERAPY': 'OccupationalTherapy',
        'ONCOLOGIC': 'Oncologic',
        'OPTOMETIC': 'Optometic',
        'OTOLARYNGOLOGIC': 'Otolaryngologic',
        'PATHOLOGY': 'Pathology',
        'PEDIATRIC': 'Pediatric',
        'PHARMACYSPECIALTY': 'PharmacySpecialty',
        'PHYSIOTHERAPY': 'Physiotherapy',
        'PLASTICSURGERY': 'PlasticSurgery',
        'PODIATRIC': 'Podiatric',
        'PSYCHIATRIC': 'Psychiatric',
        'PUBLICHEALTH': 'PublicHealth',
        'PULMONARY': 'Pulmonary',
        'RADIOGRAPY': 'Radiograpy',
        'RENAL': 'Renal',
        'RESPIRATORYTHERAPY': 'RespiratoryTherapy',
        'RHEUMATOLOGIC': 'Rheumatologic',
        'SPEECHPATHOLOGY': 'SpeechPathology',
        'SURGICAL': 'Surgical',
        'TOXICOLOGIC': 'Toxicologic',
        'UROLOGIC': 'Urologic',
        'ANESTHESIA': 'Anesthesia',
        'GYNECOLOGIC': 'Gynecologic',
        'PRIMARYCARE': 'PrimaryCare',
    }


# schema.org version 2.0
