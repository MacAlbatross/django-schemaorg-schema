# -*- coding: utf-8 -*-
from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ThingSchema(SchemaObject):

    """Schema Mixin for Thing
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The most generic type of item.
    """

    def __init__(self):
        self.schema = 'Thing'


class urlProp(SchemaProperty):

    """
    SchemaField for url
    Usage: Include in SchemaObject SchemaFields as your_django_field = urlProp()  
    schema.org description:URL of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'url'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class potentialActionProp(SchemaProperty):

    """
    SchemaField for potentialAction
    Usage: Include in SchemaObject SchemaFields as your_django_field = potentialActionProp()  
    schema.org description:Indicates a potential Action, which describes an idealized action in which this thing would play an &#39;object&#39; role.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Action"""

    _prop_schema = 'potentialAction'
    _expected_schema = 'Action'
    _enum = False
    _format_as = "ForeignKey"


class descriptionProp(SchemaProperty):

    """
    SchemaField for description
    Usage: Include in SchemaObject SchemaFields as your_django_field = descriptionProp()  
    schema.org description:A short description of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'description'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class sameAsProp(SchemaProperty):

    """
    SchemaField for sameAs
    Usage: Include in SchemaObject SchemaFields as your_django_field = sameAsProp()  
    schema.org description:URL of a reference Web page that unambiguously indicates the item&#39;s identity. E.g. the URL of the item&#39;s Wikipedia page, Freebase page, or official website.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'sameAs'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class additionalTypeProp(SchemaProperty):

    """
    SchemaField for additionalType
    Usage: Include in SchemaObject SchemaFields as your_django_field = additionalTypeProp()  
    schema.org description:An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the &#39;typeof&#39; attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'additionalType'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class alternateNameProp(SchemaProperty):

    """
    SchemaField for alternateName
    Usage: Include in SchemaObject SchemaFields as your_django_field = alternateNameProp()  
    schema.org description:An alias for the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'alternateName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class imageProp(SchemaProperty):

    """
    SchemaField for image
    Usage: Include in SchemaObject SchemaFields as your_django_field = imageProp()  
    schema.org description:URL of an image of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'image'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class nameProp(SchemaProperty):

    """
    SchemaField for name
    Usage: Include in SchemaObject SchemaFields as your_django_field = nameProp()  
    schema.org description:The name of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'name'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
