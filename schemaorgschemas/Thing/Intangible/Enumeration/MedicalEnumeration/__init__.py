# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalEnumerationSchema(SchemaObject):

    """Schema Mixin for MedicalEnumeration
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Enumerations related to health and the practice of medicine.
    """

    def __init__(self):
        self.schema = 'MedicalEnumeration'
