# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PreventionIndicationSchema(SchemaObject):

    """Schema Mixin for PreventionIndication
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An indication for preventing an underlying condition, symptom, etc.
    """

    def __init__(self):
        self.schema = 'PreventionIndication'


# schema.org version 2.0
