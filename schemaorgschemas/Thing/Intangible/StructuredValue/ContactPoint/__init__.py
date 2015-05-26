# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ContactPointSchema(SchemaObject):

    """Schema Mixin for ContactPoint
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A contact pointfor example, a Customer Complaints department.
    """

    def __init__(self):
        self.schema = 'ContactPoint'


class hoursAvailableProp(SchemaProperty):

    """
    SchemaField for hoursAvailable
    Usage: Include in SchemaObject SchemaFields as your_django_field = hoursAvailableProp()  
    schema.org description:The hours during which this contact point is available.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference OpeningHoursSpecification"""

    _prop_schema = 'hoursAvailable'
    _expected_schema = 'OpeningHoursSpecification'
    _enum = False
    _format_as = "ForeignKey"


class areaServedProp(SchemaProperty):

    """
    SchemaField for areaServed
    Usage: Include in SchemaObject SchemaFields as your_django_field = areaServedProp()  
    schema.org description:The location served by this contact point (e.g., a phone number intended for Europeans vs. North Americans or only within the United States).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AdministrativeArea"""

    _prop_schema = 'areaServed'
    _expected_schema = 'AdministrativeArea'
    _enum = False
    _format_as = "ForeignKey"


class contactTypeProp(SchemaProperty):

    """
    SchemaField for contactType
    Usage: Include in SchemaObject SchemaFields as your_django_field = contactTypeProp()  
    schema.org description:A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'contactType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class telephoneProp(SchemaProperty):

    """
    SchemaField for telephone
    Usage: Include in SchemaObject SchemaFields as your_django_field = telephoneProp()  
    schema.org description:The telephone number.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'telephone'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class productSupportedProp(SchemaProperty):

    """
    SchemaField for productSupported
    Usage: Include in SchemaObject SchemaFields as your_django_field = productSupportedProp()  
    schema.org description:The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. &quot;iPhone&quot;) or a general category of products or services (e.g. &quot;smartphones&quot;).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'productSupported'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class contactOptionProp(SchemaProperty):

    """
    SchemaField for contactOption
    Usage: Include in SchemaObject SchemaFields as your_django_field = contactOptionProp()  
    schema.org description:An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ContactPointOption"""

    _prop_schema = 'contactOption'
    _expected_schema = 'ContactPointOption'
    _enum = False
    _format_as = "ForeignKey"


class emailProp(SchemaProperty):

    """
    SchemaField for email
    Usage: Include in SchemaObject SchemaFields as your_django_field = emailProp()  
    schema.org description:Email address.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'email'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class faxNumberProp(SchemaProperty):

    """
    SchemaField for faxNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = faxNumberProp()  
    schema.org description:The fax number.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'faxNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
