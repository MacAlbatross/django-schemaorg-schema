# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.MedicalEntity.MedicalSignOrSymptom import possibleTreatmentProp, causeProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalSymptomSchema(SchemaObject):

    """Schema Mixin for MedicalSymptom
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any indication of the existence of a medical condition or disease that is apparent to the patient.
    """

    def __init__(self):
        self.schema = 'MedicalSymptom'


# schema.org version 2.0
