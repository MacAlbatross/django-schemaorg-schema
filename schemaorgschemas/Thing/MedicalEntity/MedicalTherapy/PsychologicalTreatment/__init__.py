# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy import contraindicationProp, indicationProp, adverseOutcomeProp, seriousAdverseOutcomeProp, duplicateTherapyProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PsychologicalTreatmentSchema(SchemaObject):

    """Schema Mixin for PsychologicalTreatment
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A process of care relying upon counseling, dialogue, communication, verbalization aimed at improving a mental health condition.
    """

    def __init__(self):
        self.schema = 'PsychologicalTreatment'
