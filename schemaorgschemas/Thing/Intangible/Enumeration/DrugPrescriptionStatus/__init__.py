# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrugPrescriptionStatusSchema(SchemaObject):

    """Schema Mixin for DrugPrescriptionStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Indicates whether this drug is available by prescription or over-the-counter.
    """

    def __init__(self):
        self.schema = 'DrugPrescriptionStatus'


PRESCRIPTIONSTATUS_CHOICES = (
    ('PRESCRIPTIONONLY', 'PrescriptionOnly: Available by prescription only.'),
    ('OTC', 'OTC: Available over the counter.'),
)


class prescriptionStatusProp(SchemaEnumProperty):

    """
    Enumeration for prescriptionStatus
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'prescriptionStatus'
    choices = PRESCRIPTIONSTATUS_CHOICES
    _format_as = "enum"
    adapter = {
        'PRESCRIPTIONONLY': 'PrescriptionOnly',
        'OTC': 'OTC',
    }


# schema.org version 2.0
