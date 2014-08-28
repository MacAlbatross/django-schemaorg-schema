# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PropertyValueSpecificationSchema(SchemaObject):

    """Schema Mixin for PropertyValueSpecification
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A Property value specification.
    """

    def __init__(self):
        self.schema = 'PropertyValueSpecification'


class multipleValuesProp(SchemaProperty):

    """
    SchemaField for multipleValues
    Usage: Include in SchemaObject SchemaFields as your_django_field = multipleValuesProp()  
    schema.org description:Whether multiple values are allowed for the property. Default is false.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'multipleValues'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


class stepValueProp(SchemaProperty):

    """
    SchemaField for stepValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = stepValueProp()  
    schema.org description:Specifies a regular expression for testing literal values according to the HTML spec.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'stepValue'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class valuePatternProp(SchemaProperty):

    """
    SchemaField for valuePattern
    Usage: Include in SchemaObject SchemaFields as your_django_field = valuePatternProp()  
    schema.org description:Specifies a regular expression for testing literal values according to the HTML spec.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'valuePattern'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class valueRequiredProp(SchemaProperty):

    """
    SchemaField for valueRequired
    Usage: Include in SchemaObject SchemaFields as your_django_field = valueRequiredProp()  
    schema.org description:Whether the property must be filled in to complete the action. Default is false.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Boolean"""

    _prop_schema = 'valueRequired'
    _expected_schema = 'Boolean'
    _enum = False
    _format_as = "ForeignKey"


class readonlyValueProp(SchemaProperty):

    """
    SchemaField for readonlyValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = readonlyValueProp()  
    schema.org description:Whether or not a property is mutable. Default is false. Specifying this for a property that also has a value makes it act similar to a &quot;hidden&quot; input in an HTML form.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'readonlyValue'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


class valueMaxLengthProp(SchemaProperty):

    """
    SchemaField for valueMaxLength
    Usage: Include in SchemaObject SchemaFields as your_django_field = valueMaxLengthProp()  
    schema.org description:Specifies the allowed range for number of characters in a literal value.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'valueMaxLength'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class defaultValueProp(SchemaProperty):

    """
    SchemaField for defaultValue
    Usage: Include in SchemaObject SchemaFields as your_django_field = defaultValueProp()  
    schema.org description:The default value of the input. For properties that expect a literal, the default is a literal value, for properties that expect an object, it&#39;s an ID reference to one of the current values.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Literal"""

    _prop_schema = 'defaultValue'
    _expected_schema = 'Literal'
    _enum = False
    _format_as = "ForeignKey"


class valueMinLengthProp(SchemaProperty):

    """
    SchemaField for valueMinLength
    Usage: Include in SchemaObject SchemaFields as your_django_field = valueMinLengthProp()  
    schema.org description:Specifies the minimum allowed range for number of characters in a literal value.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'valueMinLength'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


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
