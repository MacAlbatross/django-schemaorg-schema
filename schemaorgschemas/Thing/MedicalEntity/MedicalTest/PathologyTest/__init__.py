# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTest import affectedByProp, usedToDiagnoseProp, normalRangeProp, usesDeviceProp, signDetectedProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PathologyTestSchema(SchemaObject):

    """Schema Mixin for PathologyTest
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A medical test performed by a laboratory that typically involves examination of a tissue sample by a pathologist.
    """

    def __init__(self):
        self.schema = 'PathologyTest'


class tissueSampleProp(SchemaProperty):

    """
    SchemaField for tissueSample
    Usage: Include in SchemaObject SchemaFields as your_django_field = tissueSampleProp()  
    schema.org description:The type of tissue sample required for the test.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'tissueSample'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
