# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalGuideline import evidenceLevelProp, evidenceOriginProp, guidelineSubjectProp, guidelineDateProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalGuidelineContraindicationSchema(SchemaObject):

    """Schema Mixin for MedicalGuidelineContraindication
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A guideline contraindication that designates a process as harmful and where quality of the data supporting the contraindication is sound.
    """

    def __init__(self):
        self.schema = 'MedicalGuidelineContraindication'
