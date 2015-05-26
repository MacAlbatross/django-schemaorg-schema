# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DoseScheduleSchema(SchemaObject):

    """Schema Mixin for DoseSchedule
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific dosing schedule for a drug or supplement.
    """

    def __init__(self):
        self.schema = 'DoseSchedule'


class doseUnitProp(SchemaProperty):

    """
    SchemaField for doseUnit
    Usage: Include in SchemaObject SchemaFields as your_django_field = doseUnitProp()  
    schema.org description:The unit of the dose, e.g. &#39;mg&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'doseUnit'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class targetPopulationProp(SchemaProperty):

    """
    SchemaField for targetPopulation
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetPopulationProp()  
    schema.org description:Characteristics of the population for which this is intended, or which typically uses it, e.g. &#39;adults&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'targetPopulation'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class doseValueProp(SchemaProperty):

    """
    SchemaField for doseValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = doseValueProp()  
    schema.org description:The value of the dose, e.g. 500.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'doseValue'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class frequencyProp(SchemaProperty):

    """
    SchemaField for frequency
    Usage: Include in SchemaObject SchemaFields as your_django_field = frequencyProp()  
    schema.org description:How often the dose is taken, e.g. &#39;daily&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'frequency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
