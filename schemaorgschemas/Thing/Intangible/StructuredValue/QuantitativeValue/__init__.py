# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class QuantitativeValueSchema(SchemaObject):

    """Schema Mixin for QuantitativeValue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
     A point value or interval for product characteristics and other purposes.
    """

    def __init__(self):
        self.schema = 'QuantitativeValue'


class valueReferenceProp(SchemaProperty):

    """
    SchemaField for valueReference
    Usage: Include in SchemaObject SchemaFields as your_django_field = valueReferenceProp()
    schema.org description:A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference StructuredValue"""

    _prop_schema = 'valueReference'
    _expected_schema = 'StructuredValue'
    _enum = False
    _format_as = "ForeignKey"


class unitCodeProp(SchemaProperty):

    """
    SchemaField for unitCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = unitCodeProp()
    schema.org description:The unit of measurement given using the UN/CEFACT Common Code (3 characters).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'unitCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class maxValueProp(SchemaProperty):

    """
    SchemaField for maxValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = maxValueProp()
    schema.org description:The upper of the product characteristic.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'maxValue'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class valueProp(SchemaProperty):

    """
    SchemaField for value
    Usage: Include in SchemaObject SchemaFields as your_django_field = valueProp()
    schema.org description:The value of the product characteristic.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'value'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class minValueProp(SchemaProperty):

    """
    SchemaField for minValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = minValueProp()
    schema.org description:The lower value of the product characteristic.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'minValue'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"
