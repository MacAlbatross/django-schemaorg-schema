# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SeasonSchema(SchemaObject):

    """Schema Mixin for Season
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A TV or radio season.
    """

    def __init__(self):
        self.schema = 'Season'


class startDateProp(SchemaProperty):

    """
    SchemaField for startDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = startDateProp()
    schema.org description:The start date and time of the event or item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'startDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


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


class endDateProp(SchemaProperty):

    """
    SchemaField for endDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = endDateProp()
    schema.org description:The end date and time of the event or item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'endDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


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


class seasonNumberProp(SchemaProperty):

    """
    SchemaField for seasonNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = seasonNumberProp()
    schema.org description:Position of the season within an ordered group of seasons.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'seasonNumber'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


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
