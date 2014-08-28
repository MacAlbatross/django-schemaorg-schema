# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalCodeSchema(SchemaObject):

    """Schema Mixin for MedicalCode
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A code for a medical entity.
    """

    def __init__(self):
        self.schema = 'MedicalCode'


class codingSystemProp(SchemaProperty):

    """
    SchemaField for codingSystem
    Usage: Include in SchemaObject SchemaFields as your_django_field = codingSystemProp()
    schema.org description:The coding system, e.g. &#39;ICD-10&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'codingSystem'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class codeValueProp(SchemaProperty):

    """
    SchemaField for codeValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = codeValueProp()
    schema.org description:The actual code.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'codeValue'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
