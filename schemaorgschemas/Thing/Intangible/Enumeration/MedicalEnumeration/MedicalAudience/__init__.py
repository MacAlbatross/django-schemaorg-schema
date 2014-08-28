# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Audience import geographicAreaProp, audienceTypeProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.Intangible.Audience.PeopleAudience import suggestedMinAgeProp, requiredMinAgeProp, suggestedGenderProp, healthConditionProp, requiredMaxAgeProp, suggestedMaxAgeProp, requiredGenderProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalAudienceSchema(SchemaObject):

    """Schema Mixin for MedicalAudience
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Target audiences for medical web pages. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalAudience'
