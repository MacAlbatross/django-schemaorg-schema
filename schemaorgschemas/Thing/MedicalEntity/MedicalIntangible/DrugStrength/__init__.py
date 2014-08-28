# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrugStrengthSchema(SchemaObject):

    """Schema Mixin for DrugStrength
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific strength in which a medical drug is available in a specific country.
    """

    def __init__(self):
        self.schema = 'DrugStrength'


class activeIngredientProp(SchemaProperty):

    """
    SchemaField for activeIngredient
    Usage: Include in SchemaObject SchemaFields as your_django_field = activeIngredientProp()  
    schema.org description:An active ingredient, typically chemical compounds and/or biologic substances.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'activeIngredient'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class availableInProp(SchemaProperty):

    """
    SchemaField for availableIn
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableInProp()  
    schema.org description:The location in which the strength is available.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AdministrativeArea"""

    _prop_schema = 'availableIn'
    _expected_schema = 'AdministrativeArea'
    _enum = False
    _format_as = "ForeignKey"


class strengthUnitProp(SchemaProperty):

    """
    SchemaField for strengthUnit
    Usage: Include in SchemaObject SchemaFields as your_django_field = strengthUnitProp()  
    schema.org description:The units of an active ingredient&#39;s strength, e.g. mg.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'strengthUnit'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class strengthValueProp(SchemaProperty):

    """
    SchemaField for strengthValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = strengthValueProp()  
    schema.org description:The value of an active ingredient&#39;s strength, e.g. 325.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'strengthValue'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"
