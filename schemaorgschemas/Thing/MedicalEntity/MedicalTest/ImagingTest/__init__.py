# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTest import affectedByProp, usedToDiagnoseProp, normalRangeProp, usesDeviceProp, signDetectedProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ImagingTestSchema(SchemaObject):

    """Schema Mixin for ImagingTest
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any medical imaging modality typically used for diagnostic purposes.
    """

    def __init__(self):
        self.schema = 'ImagingTest'


class imagingTechniqueProp(SchemaProperty):

    """
    SchemaField for imagingTechnique
    Usage: Include in SchemaObject SchemaFields as your_django_field = imagingTechniqueProp()  
    schema.org description:Imaging technique used.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalImagingTechnique"""

    _prop_schema = 'imagingTechnique'
    _expected_schema = 'MedicalImagingTechnique'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
