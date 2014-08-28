# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AlignmentObjectSchema(SchemaObject):

    """Schema Mixin for AlignmentObject
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An intangible item that describes an alignment between a learning resource and a node in an educational framework.
    """

    def __init__(self):
        self.schema = 'AlignmentObject'


class alignmentTypeProp(SchemaProperty):

    """
    SchemaField for alignmentType
    Usage: Include in SchemaObject SchemaFields as your_django_field = alignmentTypeProp()  
    schema.org description:A category of alignment between the learning resource and the framework node. Recommended values include: &#39;assesses&#39;, &#39;teaches&#39;, &#39;requires&#39;, &#39;textComplexity&#39;, &#39;readingLevel&#39;, &#39;educationalSubject&#39;, and &#39;educationLevel&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'alignmentType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class educationalFrameworkProp(SchemaProperty):

    """
    SchemaField for educationalFramework
    Usage: Include in SchemaObject SchemaFields as your_django_field = educationalFrameworkProp()  
    schema.org description:The framework to which the resource being described is aligned.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'educationalFramework'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class targetNameProp(SchemaProperty):

    """
    SchemaField for targetName
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetNameProp()  
    schema.org description:The name of a node in an established educational framework.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'targetName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class targetDescriptionProp(SchemaProperty):

    """
    SchemaField for targetDescription
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetDescriptionProp()  
    schema.org description:The description of a node in an established educational framework.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'targetDescription'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class targetUrlProp(SchemaProperty):

    """
    SchemaField for targetUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetUrlProp()  
    schema.org description:The URL of a node in an established educational framework.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'targetUrl'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"
