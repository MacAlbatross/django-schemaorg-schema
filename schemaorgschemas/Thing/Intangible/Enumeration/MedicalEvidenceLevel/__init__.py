# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalEvidenceLevelSchema(SchemaObject):

    """Schema Mixin for MedicalEvidenceLevel
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Level of evidence for a medical guideline. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalEvidenceLevel'


/EVIDENCELEVEL_CHOICES = (
    ('/EVIDENCELEVELB', '/EvidenceLevelB'),
    ('/EVIDENCELEVELC', '/EvidenceLevelC'),
    ('/EVIDENCELEVELA', '/EvidenceLevelA'),
)


class / evidenceLevelProp(SchemaEnumProperty):

    """
    Enumeration for /evidenceLevel
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/evidenceLevel'
    choices = /EVIDENCELEVEL_CHOICES
    _format_as = "enum"
    adapter = {
        '/EVIDENCELEVELB': '/EvidenceLevelB',
        '/EVIDENCELEVELC': '/EvidenceLevelC',
        '/EVIDENCELEVELA': '/EvidenceLevelA',
    }


# schema.org version 2.0
