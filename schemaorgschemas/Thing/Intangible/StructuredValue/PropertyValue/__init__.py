# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PropertyValueSchema(SchemaObject):

    """Schema Mixin for PropertyValue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A property-value pair, e.g. representing a feature of a product or place. Use the &#39;name&#39; property for the name of the property. If there is an additional human-readable version of the value, put that into the &#39;description&#39; property.

        Always use specific schema.org properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute will typically not trigger the same effect as using the original, specific property.

    """

    def __init__(self):
        self.schema = 'PropertyValue'


class valueReferenceProp(SchemaProperty):

    """
    SchemaField for valueReference
    Usage: Include in SchemaObject SchemaFields as your_django_field = valueReferenceProp()  
    schema.org description:A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PropertyValue"""

    _prop_schema = 'valueReference'
    _expected_schema = 'PropertyValue'
    _enum = False
    _format_as = "ForeignKey"


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


class propertyIDProp(SchemaProperty):

    """
    SchemaField for propertyID
    Usage: Include in SchemaObject SchemaFields as your_django_field = propertyIDProp()  
    schema.org description:A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be (1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific id of the property), or (3) a URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry). Standards bodies should promote a standard prefix for the identifiers of properties from their standards.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'propertyID'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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
