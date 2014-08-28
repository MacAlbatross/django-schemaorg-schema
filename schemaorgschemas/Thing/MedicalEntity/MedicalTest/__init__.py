# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalTestSchema(SchemaObject):

    """Schema Mixin for MedicalTest
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any medical test, typically performed for diagnostic purposes.
    """

    def __init__(self):
        self.schema = 'MedicalTest'


class affectedByProp(SchemaProperty):

    """
    SchemaField for affectedBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = affectedByProp()  
    schema.org description:Drugs that affect the test&#39;s results.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Drug"""

    _prop_schema = 'affectedBy'
    _expected_schema = 'Drug'
    _enum = False
    _format_as = "ForeignKey"


class usedToDiagnoseProp(SchemaProperty):

    """
    SchemaField for usedToDiagnose
    Usage: Include in SchemaObject SchemaFields as your_django_field = usedToDiagnoseProp()  
    schema.org description:A condition the test is used to diagnose.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalCondition"""

    _prop_schema = 'usedToDiagnose'
    _expected_schema = 'MedicalCondition'
    _enum = False
    _format_as = "ForeignKey"


class normalRangeProp(SchemaProperty):

    """
    SchemaField for normalRange
    Usage: Include in SchemaObject SchemaFields as your_django_field = normalRangeProp()  
    schema.org description:Range of acceptable values for a typical patient, when applicable.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'normalRange'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class usesDeviceProp(SchemaProperty):

    """
    SchemaField for usesDevice
    Usage: Include in SchemaObject SchemaFields as your_django_field = usesDeviceProp()  
    schema.org description:Device used to perform the test.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalDevice"""

    _prop_schema = 'usesDevice'
    _expected_schema = 'MedicalDevice'
    _enum = False
    _format_as = "ForeignKey"


class signDetectedProp(SchemaProperty):

    """
    SchemaField for signDetected
    Usage: Include in SchemaObject SchemaFields as your_django_field = signDetectedProp()  
    schema.org description:A sign detected by the test.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalSign"""

    _prop_schema = 'signDetected'
    _expected_schema = 'MedicalSign'
    _enum = False
    _format_as = "ForeignKey"
