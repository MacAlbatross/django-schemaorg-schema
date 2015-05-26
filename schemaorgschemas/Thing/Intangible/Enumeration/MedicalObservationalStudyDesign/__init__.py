# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalObservationalStudyDesignSchema(SchemaObject):

    """Schema Mixin for MedicalObservationalStudyDesign
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Design models for observational medical studies. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalObservationalStudyDesign'


/STUDYDESIGN_CHOICES = (
    ('/COHORTSTUDY', '/CohortStudy'),
    ('/CROSSSECTIONAL', '/CrossSectional'),
    ('/LONGITUDINAL', '/Longitudinal'),
    ('/OBSERVATIONAL', '/Observational'),
    ('/REGISTRY', '/Registry'),
    ('/CASESERIES', '/CaseSeries'),
)


class / studyDesignProp(SchemaEnumProperty):

    """
    Enumeration for /studyDesign
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/studyDesign'
    choices = /STUDYDESIGN_CHOICES
    _format_as = "enum"
    adapter = {
        '/COHORTSTUDY': '/CohortStudy',
        '/CROSSSECTIONAL': '/CrossSectional',
        '/LONGITUDINAL': '/Longitudinal',
        '/OBSERVATIONAL': '/Observational',
        '/REGISTRY': '/Registry',
        '/CASESERIES': '/CaseSeries',
    }


# schema.org version 2.0
