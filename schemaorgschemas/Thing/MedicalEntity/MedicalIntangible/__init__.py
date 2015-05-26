# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalIntangibleSchema(SchemaObject):

    """Schema Mixin for MedicalIntangible
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A utility class that serves as the umbrella for a number of &#39;intangible&#39; things in the medical space.
    """

    def __init__(self):
        self.schema = 'MedicalIntangible'


# schema.org version 2.0
