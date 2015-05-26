# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.Intangible.StructuredValue.ContactPoint import productSupportedProp, contactOptionProp, telephoneProp, faxNumberProp, hoursAvailableProp, areaServedProp, contactTypeProp, emailProp, availableLanguageProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PostalAddressSchema(SchemaObject):

    """Schema Mixin for PostalAddress
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The mailing address.
    """

    def __init__(self):
        self.schema = 'PostalAddress'


class addressCountryProp(SchemaProperty):

    """
    SchemaField for addressCountry
    Usage: Include in SchemaObject SchemaFields as your_django_field = addressCountryProp()  
    schema.org description:The country. For example, USA. You can also provide the two-letter ISO 3166-1 alpha-2 country code.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Country"""

    _prop_schema = 'addressCountry'
    _expected_schema = 'Country'
    _enum = False
    _format_as = "ForeignKey"


class addressLocalityProp(SchemaProperty):

    """
    SchemaField for addressLocality
    Usage: Include in SchemaObject SchemaFields as your_django_field = addressLocalityProp()  
    schema.org description:The locality. For example, Mountain View.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'addressLocality'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class streetAddressProp(SchemaProperty):

    """
    SchemaField for streetAddress
    Usage: Include in SchemaObject SchemaFields as your_django_field = streetAddressProp()  
    schema.org description:The street address. For example, 1600 Amphitheatre Pkwy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'streetAddress'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class postOfficeBoxNumberProp(SchemaProperty):

    """
    SchemaField for postOfficeBoxNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = postOfficeBoxNumberProp()  
    schema.org description:The post office box number for PO box addresses.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'postOfficeBoxNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class postalCodeProp(SchemaProperty):

    """
    SchemaField for postalCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = postalCodeProp()  
    schema.org description:The postal code. For example, 94043.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'postalCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class addressRegionProp(SchemaProperty):

    """
    SchemaField for addressRegion
    Usage: Include in SchemaObject SchemaFields as your_django_field = addressRegionProp()  
    schema.org description:The region. For example, CA.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'addressRegion'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
