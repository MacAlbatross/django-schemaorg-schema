# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ClipSchema(SchemaObject):

    """Schema Mixin for Clip
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A short TV or radio program or a segment/part of a program.
    """

    def __init__(self):
        self.schema = 'Clip'


class clipNumberProp(SchemaProperty):

    """
    SchemaField for clipNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = clipNumberProp()
    schema.org description:Position of the clip within an ordered group of clips.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'clipNumber'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class publicationProp(SchemaProperty):

    """
    SchemaField for publication
    Usage: Include in SchemaObject SchemaFields as your_django_field = publicationProp()
    schema.org description:A publication event associated with the episode, clip or media object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PublicationEvent"""

    _prop_schema = 'publication'
    _expected_schema = 'PublicationEvent'
    _enum = False
    _format_as = "ForeignKey"


class partOfEpisodeProp(SchemaProperty):

    """
    SchemaField for partOfEpisode
    Usage: Include in SchemaObject SchemaFields as your_django_field = partOfEpisodeProp()
    schema.org description:The episode to which this clip belongs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Episode"""

    _prop_schema = 'partOfEpisode'
    _expected_schema = 'Episode'
    _enum = False
    _format_as = "ForeignKey"


class positionProp(SchemaProperty):

    """
    SchemaField for position
    Usage: Include in SchemaObject SchemaFields as your_django_field = positionProp()
    schema.org description:Free text to define other than pure numerical ranking of an episode or a season in an ordered list of items (further formatting restrictions may apply within particular user groups).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'position'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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
