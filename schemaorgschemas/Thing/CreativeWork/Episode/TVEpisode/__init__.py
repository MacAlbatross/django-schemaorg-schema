# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing.CreativeWork.Episode import episodeNumberProp, publicationProp, producerProp, productionCompanyProp, partOfSeasonProp, musicByProp, actorProp, directorProp, positionProp, partOfSeriesProp, trailerProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TVEpisodeSchema(SchemaObject):

    """Schema Mixin for TVEpisode
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A TV episode which can be part of a series or season.
    """

    def __init__(self):
        self.schema = 'TVEpisode'


class directorProp(SchemaProperty):

    """
    SchemaField for director
    Usage: Include in SchemaObject SchemaFields as your_django_field = directorProp()
    schema.org description:The director of the movie, tv/radio episode or series. Supercedes directors.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'director'
    _expected_schema = 'Person'
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


class producerProp(SchemaProperty):

    """
    SchemaField for producer
    Usage: Include in SchemaObject SchemaFields as your_django_field = producerProp()
    schema.org description:The producer of the movie, tv/radio series, season, or episode, or video.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'producer'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class productionCompanyProp(SchemaProperty):

    """
    SchemaField for productionCompany
    Usage: Include in SchemaObject SchemaFields as your_django_field = productionCompanyProp()
    schema.org description:The production company or studio that made the movie, tv/radio series, season, or episode, or media object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'productionCompany'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


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


class musicByProp(SchemaProperty):

    """
    SchemaField for musicBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicByProp()
    schema.org description:The composer of the movie or TV/radio soundtrack.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'musicBy'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class actorProp(SchemaProperty):

    """
    SchemaField for actor
    Usage: Include in SchemaObject SchemaFields as your_django_field = actorProp()
    schema.org description:A cast member of the movie, tv/radio series, season, episode, or video. Supercedes actors.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'actor'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"
