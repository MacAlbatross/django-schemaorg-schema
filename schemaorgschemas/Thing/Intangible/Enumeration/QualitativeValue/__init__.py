# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class QualitativeValueSchema(SchemaObject):

    """Schema Mixin for QualitativeValue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A predefined value for a product characteristic, e.g. the power cord plug type &quot;US&quot; or the garment sizes &quot;S&quot;, &quot;M&quot;, &quot;L&quot;, and &quot;XL&quot;.
    """

    def __init__(self):
        self.schema = 'QualitativeValue'


class lesserProp(SchemaProperty):

    """
    SchemaField for lesser
    Usage: Include in SchemaObject SchemaFields as your_django_field = lesserProp()  
    schema.org description:This ordering relation for qualitative values indicates that the subject is lesser than the object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QualitativeValue"""

    _prop_schema = 'lesser'
    _expected_schema = 'QualitativeValue'
    _enum = False
    _format_as = "TextField"


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


class greaterOrEqualProp(SchemaProperty):

    """
    SchemaField for greaterOrEqual
    Usage: Include in SchemaObject SchemaFields as your_django_field = greaterOrEqualProp()  
    schema.org description:This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QualitativeValue"""

    _prop_schema = 'greaterOrEqual'
    _expected_schema = 'QualitativeValue'
    _enum = False
    _format_as = "TextField"


class lesserOrEqualProp(SchemaProperty):

    """
    SchemaField for lesserOrEqual
    Usage: Include in SchemaObject SchemaFields as your_django_field = lesserOrEqualProp()  
    schema.org description:This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QualitativeValue"""

    _prop_schema = 'lesserOrEqual'
    _expected_schema = 'QualitativeValue'
    _enum = False
    _format_as = "TextField"


class nonEqualProp(SchemaProperty):

    """
    SchemaField for nonEqual
    Usage: Include in SchemaObject SchemaFields as your_django_field = nonEqualProp()  
    schema.org description:This ordering relation for qualitative values indicates that the subject is not equal to the object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QualitativeValue"""

    _prop_schema = 'nonEqual'
    _expected_schema = 'QualitativeValue'
    _enum = False
    _format_as = "TextField"


class equalProp(SchemaProperty):

    """
    SchemaField for equal
    Usage: Include in SchemaObject SchemaFields as your_django_field = equalProp()  
    schema.org description:This ordering relation for qualitative values indicates that the subject is equal to the object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QualitativeValue"""

    _prop_schema = 'equal'
    _expected_schema = 'QualitativeValue'
    _enum = False
    _format_as = "TextField"


class greaterProp(SchemaProperty):

    """
    SchemaField for greater
    Usage: Include in SchemaObject SchemaFields as your_django_field = greaterProp()  
    schema.org description:This ordering relation for qualitative values indicates that the subject is greater than the object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QualitativeValue"""

    _prop_schema = 'greater'
    _expected_schema = 'QualitativeValue'
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
