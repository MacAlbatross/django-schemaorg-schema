# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class QuantitativeValueSchema(SchemaObject):

    """Schema Mixin for QuantitativeValue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
     A point value or interval for product characteristics and other purposes.
    """

    def __init__(self):
        self.schema = 'QuantitativeValue'


class additionalPropertyProp(SchemaProperty):

    """
    SchemaField for additionalProperty
    Usage: Include in SchemaObject SchemaFields as your_django_field = additionalPropertyProp()  
    schema.org description:A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PropertyValue"""

    _prop_schema = 'additionalProperty'
    _expected_schema = 'PropertyValue'
    _enum = False
    _format_as = "ForeignKey"


class valueReferenceProp(SchemaProperty):

    """
    SchemaField for valueReference
    Usage: Include in SchemaObject SchemaFields as your_django_field = valueReferenceProp()  
    schema.org description:A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QualitativeValue"""

    _prop_schema = 'valueReference'
    _expected_schema = 'QualitativeValue'
    _enum = False
    _format_as = "TextField"


class unitTextProp(SchemaProperty):

    """
    SchemaField for unitText
    Usage: Include in SchemaObject SchemaFields as your_django_field = unitTextProp()  
    schema.org description:A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for unitCode.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'unitText'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class unitCodeProp(SchemaProperty):

    """
    SchemaField for unitCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = unitCodeProp()  
    schema.org description:The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.

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
    schema.org description:The upper value of some characteristic or property.

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
    schema.org description:The value of the quantitative value or property value node. For QuantitativeValue, the recommended type for values is &#39;Number&#39;. For PropertyValue, it can be &#39;Text;&#39;, &#39;Number&#39;, &#39;Boolean&#39;, or &#39;StructuredValue&#39;.

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
    schema.org description:The lower value of some characteristic or property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'minValue'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


# schema.org version 2.0
