# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTest import affectedByProp, usedToDiagnoseProp, normalRangeProp, usesDeviceProp, signDetectedProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BloodTestSchema(SchemaObject):

    """Schema Mixin for BloodTest
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A medical test performed on a sample of a patient&#39;s blood.
    """

    def __init__(self):
        self.schema = 'BloodTest'
