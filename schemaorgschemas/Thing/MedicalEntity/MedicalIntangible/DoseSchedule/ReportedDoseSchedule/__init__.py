# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalIntangible.DoseSchedule import doseUnitProp, targetPopulationProp, doseValueProp, frequencyProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReportedDoseScheduleSchema(SchemaObject):

    """Schema Mixin for ReportedDoseSchedule
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A patient-reported or observed dosing schedule for a drug or supplement.
    """

    def __init__(self):
        self.schema = 'ReportedDoseSchedule'
