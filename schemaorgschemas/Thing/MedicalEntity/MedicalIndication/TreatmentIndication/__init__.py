# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TreatmentIndicationSchema(SchemaObject):

    """Schema Mixin for TreatmentIndication
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An indication for treating an underlying condition, symptom, etc.
    """

    def __init__(self):
        self.schema = 'TreatmentIndication'


# schema.org version 2.0
