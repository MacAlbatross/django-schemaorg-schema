# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing.CreativeWork.Clip import partOfSeasonProp, publicationProp, partOfEpisodeProp, clipNumberProp, positionProp, partOfSeriesProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TVClipSchema(SchemaObject):

    """Schema Mixin for TVClip
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A short TV progam or a segment/part of a TV program.
    """

    def __init__(self):
        self.schema = 'TVClip'


class partOfSeriesProp(SchemaProperty):

    """
    SchemaField for partOfSeries
    Usage: Include in SchemaObject SchemaFields as your_django_field = partOfSeriesProp()  
    schema.org description:The series to which this episode or season belongs. Supercedes partOfTVSeries.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Series"""

    _prop_schema = 'partOfSeries'
    _expected_schema = 'Series'
    _enum = False
    _format_as = "ForeignKey"


class partOfSeasonProp(SchemaProperty):

    """
    SchemaField for partOfSeason
    Usage: Include in SchemaObject SchemaFields as your_django_field = partOfSeasonProp()  
    schema.org description:The season to which this episode belongs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Season"""

    _prop_schema = 'partOfSeason'
    _expected_schema = 'Season'
    _enum = False
    _format_as = "ForeignKey"
