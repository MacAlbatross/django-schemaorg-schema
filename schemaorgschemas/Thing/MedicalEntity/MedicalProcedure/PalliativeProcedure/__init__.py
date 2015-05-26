# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalProcedure import followupProp, preparationProp, procedureTypeProp, howPerformedProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy import contraindicationProp, indicationProp, adverseOutcomeProp, seriousAdverseOutcomeProp, duplicateTherapyProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PalliativeProcedureSchema(SchemaObject):

    """Schema Mixin for PalliativeProcedure
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A medical procedure intended primarily for palliative purposes, aimed at relieving the symptoms of an underlying health condition.
    """

    def __init__(self):
        self.schema = 'PalliativeProcedure'


# schema.org version 2.0
