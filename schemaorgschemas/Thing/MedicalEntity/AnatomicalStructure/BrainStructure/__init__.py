# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.AnatomicalStructure import functionProp, associatedPathophysiologyProp, bodyLocationProp, relatedTherapyProp, connectedToProp, partOfSystemProp, diagramProp, relatedConditionProp, subStructureProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BrainStructureSchema(SchemaObject):

    """Schema Mixin for BrainStructure
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any anatomical structure which pertains to the soft nervous tissue functioning as the coordinating center of sensation and intellectual and nervous activity.
    """

    def __init__(self):
        self.schema = 'BrainStructure'
