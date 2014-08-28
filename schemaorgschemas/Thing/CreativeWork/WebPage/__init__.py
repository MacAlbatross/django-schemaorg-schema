# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WebPageSchema(SchemaObject):

    """Schema Mixin for WebPage
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as breadcrumb may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page
    """

    def __init__(self):
        self.schema = 'WebPage'


class breadcrumbProp(SchemaProperty):

    """
    SchemaField for breadcrumb
    Usage: Include in SchemaObject SchemaFields as your_django_field = breadcrumbProp()
    schema.org description:A set of links that can help a user understand and navigate a website hierarchy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'breadcrumb'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class significantLinkProp(SchemaProperty):

    """
    SchemaField for significantLink
    Usage: Include in SchemaObject SchemaFields as your_django_field = significantLinkProp()
    schema.org description:One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most. Supercedes significantLinks.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'significantLink'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class reviewedByProp(SchemaProperty):

    """
    SchemaField for reviewedBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewedByProp()
    schema.org description:People or organizations that have reviewed the content on this web page for accuracy and/or completeness.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'reviewedBy'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class mainContentOfPageProp(SchemaProperty):

    """
    SchemaField for mainContentOfPage
    Usage: Include in SchemaObject SchemaFields as your_django_field = mainContentOfPageProp()
    schema.org description:Indicates if this web page element is the main subject of the page.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference WebPageElement"""

    _prop_schema = 'mainContentOfPage'
    _expected_schema = 'WebPageElement'
    _enum = False
    _format_as = "ForeignKey"


class isPartOfProp(SchemaProperty):

    """
    SchemaField for isPartOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = isPartOfProp()
    schema.org description:Indicates the collection or gallery to which the item belongs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CollectionPage"""

    _prop_schema = 'isPartOf'
    _expected_schema = 'CollectionPage'
    _enum = False
    _format_as = "ForeignKey"


class lastReviewedProp(SchemaProperty):

    """
    SchemaField for lastReviewed
    Usage: Include in SchemaObject SchemaFields as your_django_field = lastReviewedProp()
    schema.org description:Date on which the content on this web page was last reviewed for accuracy and/or completeness.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'lastReviewed'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class primaryImageOfPageProp(SchemaProperty):

    """
    SchemaField for primaryImageOfPage
    Usage: Include in SchemaObject SchemaFields as your_django_field = primaryImageOfPageProp()
    schema.org description:Indicates the main image on the page.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'primaryImageOfPage'
    _expected_schema = 'ImageObject'
    _enum = False
    _format_as = "URLField"


class relatedLinkProp(SchemaProperty):

    """
    SchemaField for relatedLink
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedLinkProp()
    schema.org description:A link related to this web page, for example to other related web pages.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'relatedLink'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class specialtyProp(SchemaProperty):

    """
    SchemaField for specialty
    Usage: Include in SchemaObject SchemaFields as your_django_field = specialtyProp()
    schema.org description:One of the domain specialities to which this web page&#39;s content applies.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Specialty"""

    _prop_schema = 'specialty'
    _expected_schema = 'Specialty'
    _enum = False
    _format_as = "ForeignKey"
