# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalIndicationSchema(SchemaObject):

    """Schema Mixin for MedicalIndication
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A condition or factor that indicates use of a medical therapy, including signs, symptoms, risk factors, anatomical states, etc.
    """

    def __init__(self):
        self.schema = 'MedicalIndication'
