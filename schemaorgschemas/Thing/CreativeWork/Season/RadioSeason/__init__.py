# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.Season import startDateProp, episodeProp, producerProp, productionCompanyProp, numberOfEpisodesProp, positionProp, endDateProp, partOfSeriesProp, seasonNumberProp, trailerProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RadioSeasonSchema(SchemaObject):

    """Schema Mixin for RadioSeason
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Season dedicated to radio broadcast and associated online delivery.
    """

    def __init__(self):
        self.schema = 'RadioSeason'


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


class episodeProp(SchemaProperty):

    """
    SchemaField for episode
    Usage: Include in SchemaObject SchemaFields as your_django_field = episodeProp()  
    schema.org description:An episode of a TV/radio series or season Supercedes episodes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Episode"""

    _prop_schema = 'episode'
    _expected_schema = 'Episode'
    _enum = False
    _format_as = "ForeignKey"


class trailerProp(SchemaProperty):

    """
    SchemaField for trailer
    Usage: Include in SchemaObject SchemaFields as your_django_field = trailerProp()  
    schema.org description:The trailer of a movie or tv/radio series, season, or episode.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference VideoObject"""

    _prop_schema = 'trailer'
    _expected_schema = 'VideoObject'
    _enum = False
    _format_as = "ForeignKey"


class numberOfEpisodesProp(SchemaProperty):

    """
    SchemaField for numberOfEpisodes
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfEpisodesProp()  
    schema.org description:The number of episodes in this season or series.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'numberOfEpisodes'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"
