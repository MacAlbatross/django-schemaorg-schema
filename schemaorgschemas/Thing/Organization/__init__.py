# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class OrganizationSchema(SchemaObject):

    """Schema Mixin for Organization
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An organization such as a school, NGO, corporation, club, etc.
    """

    def __init__(self):
        self.schema = 'Organization'


class isicV4Prop(SchemaProperty):

    """
    SchemaField for isicV4
    Usage: Include in SchemaObject SchemaFields as your_django_field = isicV4Prop()  
    schema.org description:The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isicV4'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class employeeProp(SchemaProperty):

    """
    SchemaField for employee
    Usage: Include in SchemaObject SchemaFields as your_django_field = employeeProp()  
    schema.org description:Someone working for this organization. Supersedes employees.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'employee'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class numberOfEmployeesProp(SchemaProperty):

    """
    SchemaField for numberOfEmployees
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfEmployeesProp()  
    schema.org description:The number of employees in an organization e.g. business.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'numberOfEmployees'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class subOrganizationProp(SchemaProperty):

    """
    SchemaField for subOrganization
    Usage: Include in SchemaObject SchemaFields as your_django_field = subOrganizationProp()  
    schema.org description:A relationship between two organizations where the first includes the second, e.g., as a subsidiary. See also: the more specific &#39;department&#39; property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'subOrganization'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class brandProp(SchemaProperty):

    """
    SchemaField for brand
    Usage: Include in SchemaObject SchemaFields as your_django_field = brandProp()  
    schema.org description:The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'brand'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class legalNameProp(SchemaProperty):

    """
    SchemaField for legalName
    Usage: Include in SchemaObject SchemaFields as your_django_field = legalNameProp()  
    schema.org description:The official name of the organization, e.g. the registered company name.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'legalName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class foundingDateProp(SchemaProperty):

    """
    SchemaField for foundingDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = foundingDateProp()  
    schema.org description:The date that this organization was founded.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'foundingDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


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


class awardProp(SchemaProperty):

    """
    SchemaField for award
    Usage: Include in SchemaObject SchemaFields as your_django_field = awardProp()  
    schema.org description:An award won by or for this item. Supersedes awards.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'award'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class aggregateRatingProp(SchemaProperty):

    """
    SchemaField for aggregateRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = aggregateRatingProp()  
    schema.org description:The overall rating, based on a collection of reviews or ratings, of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AggregateRating"""

    _prop_schema = 'aggregateRating'
    _expected_schema = 'AggregateRating'
    _enum = False
    _format_as = "ForeignKey"


class dissolutionDateProp(SchemaProperty):

    """
    SchemaField for dissolutionDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = dissolutionDateProp()  
    schema.org description:The date that this organization was dissolved.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dissolutionDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class addressProp(SchemaProperty):

    """
    SchemaField for address
    Usage: Include in SchemaObject SchemaFields as your_django_field = addressProp()  
    schema.org description:Physical address of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PostalAddress"""

    _prop_schema = 'address'
    _expected_schema = 'PostalAddress'
    _enum = False
    _format_as = "ForeignKey"


class dunsProp(SchemaProperty):

    """
    SchemaField for duns
    Usage: Include in SchemaObject SchemaFields as your_django_field = dunsProp()  
    schema.org description:The Dun &amp; Bradstreet DUNS number for identifying an organization or business person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'duns'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class logoProp(SchemaProperty):

    """
    SchemaField for logo
    Usage: Include in SchemaObject SchemaFields as your_django_field = logoProp()  
    schema.org description:An associated logo.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'logo'
    _expected_schema = 'ImageObject'
    _enum = False
    _format_as = "URLField"


class contactPointProp(SchemaProperty):

    """
    SchemaField for contactPoint
    Usage: Include in SchemaObject SchemaFields as your_django_field = contactPointProp()  
    schema.org description:A contact point for a person or organization. Supersedes contactPoints.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ContactPoint"""

    _prop_schema = 'contactPoint'
    _expected_schema = 'ContactPoint'
    _enum = False
    _format_as = "ForeignKey"


class eventProp(SchemaProperty):

    """
    SchemaField for event
    Usage: Include in SchemaObject SchemaFields as your_django_field = eventProp()  
    schema.org description:Upcoming or past event associated with this place, organization, or action. Supersedes events.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Event"""

    _prop_schema = 'event'
    _expected_schema = 'Event'
    _enum = False
    _format_as = "ForeignKey"


class makesOfferProp(SchemaProperty):

    """
    SchemaField for makesOffer
    Usage: Include in SchemaObject SchemaFields as your_django_field = makesOfferProp()  
    schema.org description:A pointer to products or services offered by the organization or person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Offer"""

    _prop_schema = 'makesOffer'
    _expected_schema = 'Offer'
    _enum = False
    _format_as = "ForeignKey"


class hasPOSProp(SchemaProperty):

    """
    SchemaField for hasPOS
    Usage: Include in SchemaObject SchemaFields as your_django_field = hasPOSProp()  
    schema.org description:Points-of-Sales operated by the organization or person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'hasPOS'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class founderProp(SchemaProperty):

    """
    SchemaField for founder
    Usage: Include in SchemaObject SchemaFields as your_django_field = founderProp()  
    schema.org description:A person who founded this organization. Supersedes founders.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'founder'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class naicsProp(SchemaProperty):

    """
    SchemaField for naics
    Usage: Include in SchemaObject SchemaFields as your_django_field = naicsProp()  
    schema.org description:The North American Industry Classification System (NAICS) code for a particular organization or business person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'naics'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class memberOfProp(SchemaProperty):

    """
    SchemaField for memberOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = memberOfProp()  
    schema.org description:An Organization (or ProgramMembership) to which this Person or Organization belongs. Inverse property: member.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'memberOf'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class reviewProp(SchemaProperty):

    """
    SchemaField for review
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewProp()  
    schema.org description:A review of the item. Supersedes reviews.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Review"""

    _prop_schema = 'review'
    _expected_schema = 'Review'
    _enum = False
    _format_as = "ForeignKey"


class taxIDProp(SchemaProperty):

    """
    SchemaField for taxID
    Usage: Include in SchemaObject SchemaFields as your_django_field = taxIDProp()  
    schema.org description:The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'taxID'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class memberProp(SchemaProperty):

    """
    SchemaField for member
    Usage: Include in SchemaObject SchemaFields as your_django_field = memberProp()  
    schema.org description:A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals. Supersedes musicGroupMember, members. Inverse property: memberOf.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'member'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class foundingLocationProp(SchemaProperty):

    """
    SchemaField for foundingLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = foundingLocationProp()  
    schema.org description:The place where the Organization was founded.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'foundingLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class locationProp(SchemaProperty):

    """
    SchemaField for location
    Usage: Include in SchemaObject SchemaFields as your_django_field = locationProp()  
    schema.org description:The location of the event, organization or action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'location'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class ownsProp(SchemaProperty):

    """
    SchemaField for owns
    Usage: Include in SchemaObject SchemaFields as your_django_field = ownsProp()  
    schema.org description:Products owned by the organization or person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'owns'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


class departmentProp(SchemaProperty):

    """
    SchemaField for department
    Usage: Include in SchemaObject SchemaFields as your_django_field = departmentProp()  
    schema.org description:A relationship between an organization and a department of that organization, also described as an organization (allowing different urls, logos, opening hours). For example: a store with a pharmacy, or a bakery with a cafe.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'department'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class vatIDProp(SchemaProperty):

    """
    SchemaField for vatID
    Usage: Include in SchemaObject SchemaFields as your_django_field = vatIDProp()  
    schema.org description:The Value-added Tax ID of the organization or person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'vatID'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class seeksProp(SchemaProperty):

    """
    SchemaField for seeks
    Usage: Include in SchemaObject SchemaFields as your_django_field = seeksProp()  
    schema.org description:A pointer to products or services sought by the organization or person (demand).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Demand"""

    _prop_schema = 'seeks'
    _expected_schema = 'Demand'
    _enum = False
    _format_as = "ForeignKey"


class globalLocationNumberProp(SchemaProperty):

    """
    SchemaField for globalLocationNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = globalLocationNumberProp()  
    schema.org description:The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'globalLocationNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
