# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ReviewSchema(SchemaObject):

    """Schema Mixin for Review
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A review of an item - for example, a restaurant, movie, or store.
    """

    def __init__(self):
        self.schema = 'Review'


class reviewBodyProp(SchemaProperty):

    """
    SchemaField for reviewBody
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewBodyProp()
    schema.org description:The actual body of the review.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'reviewBody'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class itemReviewedProp(SchemaProperty):

    """
    SchemaField for itemReviewed
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemReviewedProp()
    schema.org description:The item that is being reviewed/rated.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'itemReviewed'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class reviewRatingProp(SchemaProperty):

    """
    SchemaField for reviewRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewRatingProp()
    schema.org description:The rating given in this review. Note that reviews can themselves be rated. The reviewRating applies to rating given by the review. The aggregateRating property applies to the review itself, as a creative work.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Rating"""

    _prop_schema = 'reviewRating'
    _expected_schema = 'Rating'
    _enum = False
    _format_as = "ForeignKey"
