# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalDevicePurposeSchema(SchemaObject):

    """Schema Mixin for MedicalDevicePurpose
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Categories of medical devices, organized by the purpose or intended use of the device.
    """

    def __init__(self):
        self.schema = 'MedicalDevicePurpose'


PURPOSE_CHOICES = (
    ('DIAGNOSTIC',
     'Diagnostic: A medical device used for diagnostic purposes.'),
    ('THERAPEUTIC',
     'Therapeutic: A medical device used for therapeutic purposes.'),
)


class purposeProp(SchemaEnumProperty):

    """
    Enumeration for purpose
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'purpose'
    choices = PURPOSE_CHOICES
    _format_as = "enum"
    adapter = {
        'DIAGNOSTIC': 'Diagnostic',
        'THERAPEUTIC': 'Therapeutic',
    }


# schema.org version 2.0
