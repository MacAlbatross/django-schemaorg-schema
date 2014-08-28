# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PersonSchema(SchemaObject):

    """Schema Mixin for Person
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A person (alive, dead, undead, or fictional).
    """

    def __init__(self):
        self.schema = 'Person'


class honorificPrefixProp(SchemaProperty):

    """
    SchemaField for honorificPrefix
    Usage: Include in SchemaObject SchemaFields as your_django_field = honorificPrefixProp()  
    schema.org description:An honorific prefix preceding a Person&#39;s name such as Dr/Mrs/Mr.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'honorificPrefix'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class followsProp(SchemaProperty):

    """
    SchemaField for follows
    Usage: Include in SchemaObject SchemaFields as your_django_field = followsProp()  
    schema.org description:The most generic uni-directional social relation.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'follows'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class relatedToProp(SchemaProperty):

    """
    SchemaField for relatedTo
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedToProp()  
    schema.org description:The most generic familial relation.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'relatedTo'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class interactionCountProp(SchemaProperty):

    """
    SchemaField for interactionCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = interactionCountProp()  
    schema.org description:A count of a specific user interactions with this item-for example, 20 UserLikes, 5 UserComments, or 300 UserDownloads. The user interaction type should be one of the sub types of UserInteraction.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'interactionCount'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class birthDateProp(SchemaProperty):

    """
    SchemaField for birthDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = birthDateProp()  
    schema.org description:Date of birth.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'birthDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


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


class siblingProp(SchemaProperty):

    """
    SchemaField for sibling
    Usage: Include in SchemaObject SchemaFields as your_django_field = siblingProp()  
    schema.org description:A sibling of the person. Supercedes siblings.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'sibling'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class additionalNameProp(SchemaProperty):

    """
    SchemaField for additionalName
    Usage: Include in SchemaObject SchemaFields as your_django_field = additionalNameProp()  
    schema.org description:An additional name for a Person, can be used for a middle name.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'additionalName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class workLocationProp(SchemaProperty):

    """
    SchemaField for workLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = workLocationProp()  
    schema.org description:A contact location for a person&#39;s place of work.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ContactPoint"""

    _prop_schema = 'workLocation'
    _expected_schema = 'ContactPoint'
    _enum = False
    _format_as = "ForeignKey"


class genderProp(SchemaProperty):

    """
    SchemaField for gender
    Usage: Include in SchemaObject SchemaFields as your_django_field = genderProp()  
    schema.org description:Gender of the person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gender'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class childrenProp(SchemaProperty):

    """
    SchemaField for children
    Usage: Include in SchemaObject SchemaFields as your_django_field = childrenProp()  
    schema.org description:A child of the person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'children'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


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


class spouseProp(SchemaProperty):

    """
    SchemaField for spouse
    Usage: Include in SchemaObject SchemaFields as your_django_field = spouseProp()  
    schema.org description:The person&#39;s spouse.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'spouse'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class worksForProp(SchemaProperty):

    """
    SchemaField for worksFor
    Usage: Include in SchemaObject SchemaFields as your_django_field = worksForProp()  
    schema.org description:Organizations that the person works for.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'worksFor'
    _expected_schema = 'Organization'
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


class honorificSuffixProp(SchemaProperty):

    """
    SchemaField for honorificSuffix
    Usage: Include in SchemaObject SchemaFields as your_django_field = honorificSuffixProp()  
    schema.org description:An honorific suffix preceding a Person&#39;s name such as M.D. /PhD/MSCSW.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'honorificSuffix'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class homeLocationProp(SchemaProperty):

    """
    SchemaField for homeLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = homeLocationProp()  
    schema.org description:A contact location for a person&#39;s residence.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ContactPoint"""

    _prop_schema = 'homeLocation'
    _expected_schema = 'ContactPoint'
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


class colleagueProp(SchemaProperty):

    """
    SchemaField for colleague
    Usage: Include in SchemaObject SchemaFields as your_django_field = colleagueProp()  
    schema.org description:A colleague of the person. Supercedes colleagues.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'colleague'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class performerInProp(SchemaProperty):

    """
    SchemaField for performerIn
    Usage: Include in SchemaObject SchemaFields as your_django_field = performerInProp()  
    schema.org description:Event that this person is a performer or participant in.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Event"""

    _prop_schema = 'performerIn'
    _expected_schema = 'Event'
    _enum = False
    _format_as = "ForeignKey"


class knowsProp(SchemaProperty):

    """
    SchemaField for knows
    Usage: Include in SchemaObject SchemaFields as your_django_field = knowsProp()  
    schema.org description:The most generic bi-directional social/work relation.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'knows'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class parentProp(SchemaProperty):

    """
    SchemaField for parent
    Usage: Include in SchemaObject SchemaFields as your_django_field = parentProp()  
    schema.org description:A parent of this person. Supercedes parents.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'parent'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class jobTitleProp(SchemaProperty):

    """
    SchemaField for jobTitle
    Usage: Include in SchemaObject SchemaFields as your_django_field = jobTitleProp()  
    schema.org description:The job title of the person (for example, Financial Manager).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'jobTitle'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class brandProp(SchemaProperty):

    """
    SchemaField for brand
    Usage: Include in SchemaObject SchemaFields as your_django_field = brandProp()  
    schema.org description:The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Brand"""

    _prop_schema = 'brand'
    _expected_schema = 'Brand'
    _enum = False
    _format_as = "ForeignKey"


class familyNameProp(SchemaProperty):

    """
    SchemaField for familyName
    Usage: Include in SchemaObject SchemaFields as your_django_field = familyNameProp()  
    schema.org description:Family name. In the U.S., the last name of an Person. This can be used along with givenName instead of the Name property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'familyName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class awardProp(SchemaProperty):

    """
    SchemaField for award
    Usage: Include in SchemaObject SchemaFields as your_django_field = awardProp()  
    schema.org description:An award won by this person or for this creative work. Supercedes awards.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'award'
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


class nationalityProp(SchemaProperty):

    """
    SchemaField for nationality
    Usage: Include in SchemaObject SchemaFields as your_django_field = nationalityProp()  
    schema.org description:Nationality of the person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Country"""

    _prop_schema = 'nationality'
    _expected_schema = 'Country'
    _enum = False
    _format_as = "ForeignKey"


class contactPointProp(SchemaProperty):

    """
    SchemaField for contactPoint
    Usage: Include in SchemaObject SchemaFields as your_django_field = contactPointProp()  
    schema.org description:A contact point for a person or organization. Supercedes contactPoints.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ContactPoint"""

    _prop_schema = 'contactPoint'
    _expected_schema = 'ContactPoint'
    _enum = False
    _format_as = "ForeignKey"


class deathDateProp(SchemaProperty):

    """
    SchemaField for deathDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = deathDateProp()  
    schema.org description:Date of death.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'deathDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


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


class givenNameProp(SchemaProperty):

    """
    SchemaField for givenName
    Usage: Include in SchemaObject SchemaFields as your_django_field = givenNameProp()  
    schema.org description:Given name. In the U.S., the first name of a Person. This can be used along with familyName instead of the Name property.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'givenName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class affiliationProp(SchemaProperty):

    """
    SchemaField for affiliation
    Usage: Include in SchemaObject SchemaFields as your_django_field = affiliationProp()  
    schema.org description:An organization that this person is affiliated with. For example, a school/university, a club, or a team.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'affiliation'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class memberOfProp(SchemaProperty):

    """
    SchemaField for memberOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = memberOfProp()  
    schema.org description:An organization to which the person belongs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'memberOf'
    _expected_schema = 'Organization'
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


class vatIDProp(SchemaProperty):

    """
    SchemaField for vatID
    Usage: Include in SchemaObject SchemaFields as your_django_field = vatIDProp()  
    schema.org description:The Value-added Tax ID of the organisation or person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'vatID'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class alumniOfProp(SchemaProperty):

    """
    SchemaField for alumniOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = alumniOfProp()  
    schema.org description:An educational organizations that the person is an alumni of.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference EducationalOrganization"""

    _prop_schema = 'alumniOf'
    _expected_schema = 'EducationalOrganization'
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
