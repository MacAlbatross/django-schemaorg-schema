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


class sameAsProp(SchemaProperty):

    """
    SchemaField for sameAs
    Usage: Include in SchemaObject SchemaFields as your_django_field = sameAsProp()  
    schema.org description:URL of a reference Web page that unambiguously indicates the item&#39;s identity. E.g. the URL of the item&#39;s Wikipedia page, Freebase page, or official website.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'sameAs'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


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


class mainEntityOfPageProp(SchemaProperty):

    """
    SchemaField for mainEntityOfPage
    Usage: Include in SchemaObject SchemaFields as your_django_field = mainEntityOfPageProp()  
    schema.org description:Indicates a page (or other CreativeWork) for which this thing is the main entity being described. Many (but not all) pages have a fairly clear primary topic, some entity or thing that the page describes. For example a restaurant&#39;s home page might be primarily about that Restaurant, or an event listing page might represent a single event. The mainEntity and mainEntityOfPage properties allow you to explicitly express the relationship between the page and the primary entity.  Related properties include sameAs, about, and url.  The sameAs and url properties are both similar to mainEntityOfPage. The url property should be reserved to refer to more official or authoritative web pages, such as the item&#39;s official website. The sameAs property also relates a thing to a page that indirectly identifies it. Whereas sameAs emphasises well known pages, the mainEntityOfPage property serves more to clarify which of several entities is the main one for that page.  mainEntityOfPage can be used for any page, including those not recognized as authoritative for that entity. For example, for a product, sameAs might refer to a page on the manufacturer&#39;s official site with specs for the product, while mainEntityOfPage might be used on pages within various retailers&#39; sites giving details for the same product.  about is similar to mainEntity, with two key differences. First, about can refer to multiple entities/topics, while mainEntity should be used for only the primary one. Second, some pages have a primary entity that itself describes some other entity. For example, one web page may display a news article about a particular person. Another page may display a product review for a particular product. In these cases, mainEntity for the pages should refer to the news article or review, respectively, while about would more properly refer to the person or product. Inverse property: mainEntity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'mainEntityOfPage'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class additionalTypeProp(SchemaProperty):

    """
    SchemaField for additionalType
    Usage: Include in SchemaObject SchemaFields as your_django_field = additionalTypeProp()  
    schema.org description:An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the &#39;typeof&#39; attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'additionalType'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


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


class urlProp(SchemaProperty):

    """
    SchemaField for url
    Usage: Include in SchemaObject SchemaFields as your_django_field = urlProp()  
    schema.org description:URL of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'url'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class imageProp(SchemaProperty):

    """
    SchemaField for image
    Usage: Include in SchemaObject SchemaFields as your_django_field = imageProp()  
    schema.org description:An image of the item. This can be a URL or a fully described ImageObject.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'image'
    _expected_schema = 'ImageObject'
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


# schema.org version 2.0
