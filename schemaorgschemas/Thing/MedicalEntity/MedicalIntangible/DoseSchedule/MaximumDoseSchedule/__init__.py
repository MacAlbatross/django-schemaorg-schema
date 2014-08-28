# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalIntangible.DoseSchedule import doseUnitProp, targetPopulationProp, doseValueProp, frequencyProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MaximumDoseScheduleSchema(SchemaObject):

    """Schema Mixin for MaximumDoseSchedule
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The maximum dosing schedule considered safe for a drug or supplement as recommended by an authority or by the drug/supplement&#39;s manufacturer. Capture the recommending authority in the recognizingAuthority property of MedicalEntity.
    """

    def __init__(self):
        self.schema = 'MaximumDoseSchedule'
