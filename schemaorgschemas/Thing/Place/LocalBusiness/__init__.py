# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, urlProp, imageProp, sameAsProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LocalBusinessSchema(SchemaObject):

    """Schema Mixin for LocalBusiness
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.
    """

    def __init__(self):
        self.schema = 'LocalBusiness'


class priceRangeProp(SchemaProperty):

    """
    SchemaField for priceRange
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceRangeProp()  
    schema.org description:The price range of the business, for example $$$.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'priceRange'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class parentOrganizationProp(SchemaProperty):

    """
    SchemaField for parentOrganization
    Usage: Include in SchemaObject SchemaFields as your_django_field = parentOrganizationProp()  
    schema.org description:The larger organization that this local business is a branch of, if any. Supersedes branchOf.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'parentOrganization'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class currenciesAcceptedProp(SchemaProperty):

    """
    SchemaField for currenciesAccepted
    Usage: Include in SchemaObject SchemaFields as your_django_field = currenciesAcceptedProp()  
    schema.org description:The currency accepted (in ISO 4217 currency format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'currenciesAccepted'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class openingHoursProp(SchemaProperty):

    """
    SchemaField for openingHours
    Usage: Include in SchemaObject SchemaFields as your_django_field = openingHoursProp()  
    schema.org description:The opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas &#39;,&#39; separating each day. Day or time ranges are specified using a hyphen &#39;-&#39;.- Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su.- Times are specified using 24:00 time. For example, 3pm is specified as 15:00. - Here is an example: &lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;. - If a business is open 7 days a week, then it can be specified as &lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'openingHours'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class paymentAcceptedProp(SchemaProperty):

    """
    SchemaField for paymentAccepted
    Usage: Include in SchemaObject SchemaFields as your_django_field = paymentAcceptedProp()  
    schema.org description:Cash, credit card, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'paymentAccepted'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
