# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalImagingTechniqueSchema(SchemaObject):

    """Schema Mixin for MedicalImagingTechnique
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any medical imaging modality typically used for diagnostic purposes. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalImagingTechnique'


IMAGINGTECHNIQUE_CHOICES = (
    ('MRI', 'MRI: Magnetic resonance imaging.'),
    ('PET', 'PET: Positron emission tomography imaging.'),
    ('ULTRASOUND', 'Ultrasound: Ultrasound imaging.'),
    ('XRAY', 'XRay: X-ray imaging.'),
    ('CT', 'CT: X-ray computed tomography imaging.'),
)


class imagingTechniqueProp(SchemaEnumProperty):

    """
    Enumeration for imagingTechnique
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'imagingTechnique'
    choices = IMAGINGTECHNIQUE_CHOICES
    _format_as = "enum"
    adapter = {
        'MRI': 'MRI',
        'PET': 'PET',
        'ULTRASOUND': 'Ultrasound',
        'XRAY': 'XRay',
        'CT': 'CT',
    }
