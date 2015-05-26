# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicineSystemSchema(SchemaObject):

    """Schema Mixin for MedicineSystem
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Systems of medical practice.
    """

    def __init__(self):
        self.schema = 'MedicineSystem'


/MEDICINESYSTEM_CHOICES = (
    ('/CHIROPRACTIC', '/Chiropractic'),
    ('/HOMEOPATHIC', '/Homeopathic'),
    ('/OSTEOPATHIC', '/Osteopathic'),
    ('/TRADITIONALCHINESE', '/TraditionalChinese'),
    ('/WESTERNCONVENTIONAL', '/WesternConventional'),
    ('/AYURVEDIC', '/Ayurvedic'),
)


class / medicineSystemProp(SchemaEnumProperty):

    """
    Enumeration for /medicineSystem
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/medicineSystem'
    choices = /MEDICINESYSTEM_CHOICES
    _format_as = "enum"
    adapter = {
        '/CHIROPRACTIC': '/Chiropractic',
        '/HOMEOPATHIC': '/Homeopathic',
        '/OSTEOPATHIC': '/Osteopathic',
        '/TRADITIONALCHINESE': '/TraditionalChinese',
        '/WESTERNCONVENTIONAL': '/WesternConventional',
        '/AYURVEDIC': '/Ayurvedic',
    }


# schema.org version 2.0
