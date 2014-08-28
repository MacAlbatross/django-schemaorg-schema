# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalRiskFactorSchema(SchemaObject):

    """Schema Mixin for MedicalRiskFactor
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A risk factor is anything that increases a person&#39;s likelihood of developing or contracting a disease, medical condition, or complication.
    """

    def __init__(self):
        self.schema = 'MedicalRiskFactor'


class increasesRiskOfProp(SchemaProperty):

    """
    SchemaField for increasesRiskOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = increasesRiskOfProp()
    schema.org description:The condition, complication, etc. influenced by this factor.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalEntity"""

    _prop_schema = 'increasesRiskOf'
    _expected_schema = 'MedicalEntity'
    _enum = False
    _format_as = "ForeignKey"
