# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalSignOrSymptomSchema(SchemaObject):

    """Schema Mixin for MedicalSignOrSymptom
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any indication of the existence of a medical condition or disease.
    """

    def __init__(self):
        self.schema = 'MedicalSignOrSymptom'


class possibleTreatmentProp(SchemaProperty):

    """
    SchemaField for possibleTreatment
    Usage: Include in SchemaObject SchemaFields as your_django_field = possibleTreatmentProp()  
    schema.org description:A possible treatment to address this condition, sign or symptom.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTherapy"""

    _prop_schema = 'possibleTreatment'
    _expected_schema = 'MedicalTherapy'
    _enum = False
    _format_as = "ForeignKey"


class causeProp(SchemaProperty):

    """
    SchemaField for cause
    Usage: Include in SchemaObject SchemaFields as your_django_field = causeProp()  
    schema.org description:An underlying cause. More specifically, one of the causative agent(s) that are most directly responsible for the pathophysiologic process that eventually results in the occurrence.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalCause"""

    _prop_schema = 'cause'
    _expected_schema = 'MedicalCause'
    _enum = False
    _format_as = "ForeignKey"
