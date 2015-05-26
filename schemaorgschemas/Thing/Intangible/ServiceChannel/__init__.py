# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ServiceChannelSchema(SchemaObject):

    """Schema Mixin for ServiceChannel
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A means for accessing a service, e.g. a government office location, web site, or phone number.
    """

    def __init__(self):
        self.schema = 'ServiceChannel'


class processingTimeProp(SchemaProperty):

    """
    SchemaField for processingTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = processingTimeProp()  
    schema.org description:Estimated processing time for the service using this channel.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'processingTime'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class serviceLocationProp(SchemaProperty):

    """
    SchemaField for serviceLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = serviceLocationProp()  
    schema.org description:The location (e.g. civic structure, local business, etc.) where a person can go to access the service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'serviceLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class providesServiceProp(SchemaProperty):

    """
    SchemaField for providesService
    Usage: Include in SchemaObject SchemaFields as your_django_field = providesServiceProp()  
    schema.org description:The service provided by this channel.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Service"""

    _prop_schema = 'providesService'
    _expected_schema = 'Service'
    _enum = False
    _format_as = "ForeignKey"


class serviceUrlProp(SchemaProperty):

    """
    SchemaField for serviceUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = serviceUrlProp()  
    schema.org description:The website to access the service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'serviceUrl'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class servicePhoneProp(SchemaProperty):

    """
    SchemaField for servicePhone
    Usage: Include in SchemaObject SchemaFields as your_django_field = servicePhoneProp()  
    schema.org description:The phone number to use to access the service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ContactPoint"""

    _prop_schema = 'servicePhone'
    _expected_schema = 'ContactPoint'
    _enum = False
    _format_as = "ForeignKey"


class servicePostalAddressProp(SchemaProperty):

    """
    SchemaField for servicePostalAddress
    Usage: Include in SchemaObject SchemaFields as your_django_field = servicePostalAddressProp()  
    schema.org description:The address for accessing the service by mail.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PostalAddress"""

    _prop_schema = 'servicePostalAddress'
    _expected_schema = 'PostalAddress'
    _enum = False
    _format_as = "ForeignKey"


class availableLanguageProp(SchemaProperty):

    """
    SchemaField for availableLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableLanguageProp()  
    schema.org description:A language someone may use with the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Language"""

    _prop_schema = 'availableLanguage'
    _expected_schema = 'Language'
    _enum = False
    _format_as = "ForeignKey"


class serviceSmsNumberProp(SchemaProperty):

    """
    SchemaField for serviceSmsNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = serviceSmsNumberProp()  
    schema.org description:The number to access the service by text message.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ContactPoint"""

    _prop_schema = 'serviceSmsNumber'
    _expected_schema = 'ContactPoint'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
