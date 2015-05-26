# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalImagingTechniqueSchema(SchemaObject):

    """Schema Mixin for MedicalImagingTechnique
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any medical imaging modality typically used for diagnostic purposes. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalImagingTechnique'


/IMAGINGTECHNIQUE_CHOICES = (
    ('/MRI', '/MRI'),
    ('/PET', '/PET'),
    ('/ULTRASOUND', '/Ultrasound'),
    ('/XRAY', '/XRay'),
    ('/CT', '/CT'),
)


class / imagingTechniqueProp(SchemaEnumProperty):

    """
    Enumeration for /imagingTechnique
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/imagingTechnique'
    choices = /IMAGINGTECHNIQUE_CHOICES
    _format_as = "enum"
    adapter = {
        '/MRI': '/MRI',
        '/PET': '/PET',
        '/ULTRASOUND': '/Ultrasound',
        '/XRAY': '/XRay',
        '/CT': '/CT',
    }


# schema.org version 2.0
