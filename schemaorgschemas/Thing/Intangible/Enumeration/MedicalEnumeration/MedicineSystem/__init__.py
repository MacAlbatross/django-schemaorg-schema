# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicineSystemSchema(SchemaObject):

    """Schema Mixin for MedicineSystem
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Systems of medical practice.
    """

    def __init__(self):
        self.schema = 'MedicineSystem'


MEDICINESYSTEM_CHOICES = (
    ('CHIROPRACTIC',
     'Chiropractic: A system of medicine focused on the relationship between the body&#39;s structure, mainly the spine, and its functioning.'),
    ('HOMEOPATHIC',
     'Homeopathic: A system of medicine based on the principle that a disease can be cured by a substance that produces similar symptoms in healthy people.'),
    ('OSTEOPATHIC',
     'Osteopathic: A system of medicine focused on promoting the body&#39;s innate ability to heal itself.'),
    ('TRADITIONALCHINESE',
     'TraditionalChinese: A system of medicine based on common theoretical concepts that originated in China and evolved over thousands of years, that uses herbs, acupuncture, exercise, massage, dietary therapy, and other methods to treat a wide range of conditions.'),
    ('WESTERNCONVENTIONAL',
     'WesternConventional: The conventional Western system of medicine, that aims to apply the best available evidence gained from the scientific method to clinical decision making. Also known as conventional or Western medicine.'),
    ('AYURVEDIC',
     'Ayurvedic: A system of medicine that originated in India over thousands of years and that focuses on integrating and balancing the body, mind, and spirit.'),
)


class medicineSystemProp(SchemaEnumProperty):

    """
    Enumeration for medicineSystem
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'medicineSystem'
    choices = MEDICINESYSTEM_CHOICES
    _format_as = "enum"
    adapter = {
        'CHIROPRACTIC': 'Chiropractic',
        'HOMEOPATHIC': 'Homeopathic',
        'OSTEOPATHIC': 'Osteopathic',
        'TRADITIONALCHINESE': 'TraditionalChinese',
        'WESTERNCONVENTIONAL': 'WesternConventional',
        'AYURVEDIC': 'Ayurvedic',
    }
