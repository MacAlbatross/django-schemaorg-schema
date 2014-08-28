# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.Series import startDateProp, episodeProp, numberOfSeasonsProp, producerProp, productionCompanyProp, seasonProp, musicByProp, actorProp, directorProp, numberOfEpisodesProp, endDateProp, trailerProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TVSeriesSchema(SchemaObject):

    """Schema Mixin for TVSeries
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Series dedicated to TV broadcast and associated online delivery.
    """

    def __init__(self):
        self.schema = 'TVSeries'


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


class seasonProp(SchemaProperty):

    """
    SchemaField for season
    Usage: Include in SchemaObject SchemaFields as your_django_field = seasonProp()  
    schema.org description:A season in a tv/radio series. Supercedes seasons.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Season"""

    _prop_schema = 'season'
    _expected_schema = 'Season'
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
