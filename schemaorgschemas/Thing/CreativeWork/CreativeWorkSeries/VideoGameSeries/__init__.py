# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing.CreativeWork.CreativeWorkSeries import startDateProp, endDateProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VideoGameSeriesSchema(SchemaObject):

    """Schema Mixin for VideoGameSeries
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A video game series.
    """

    def __init__(self):
        self.schema = 'VideoGameSeries'


class containsSeasonProp(SchemaProperty):

    """
    SchemaField for containsSeason
    Usage: Include in SchemaObject SchemaFields as your_django_field = containsSeasonProp()  
    schema.org description:A season that is part of the media series. Supersedes season.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWorkSeason"""

    _prop_schema = 'containsSeason'
    _expected_schema = 'CreativeWorkSeason'
    _enum = False
    _format_as = "ForeignKey"


class cheatCodeProp(SchemaProperty):

    """
    SchemaField for cheatCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = cheatCodeProp()  
    schema.org description:Cheat codes to the game.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWork"""

    _prop_schema = 'cheatCode'
    _expected_schema = 'CreativeWork'
    _enum = False
    _format_as = "ForeignKey"


class episodeProp(SchemaProperty):

    """
    SchemaField for episode
    Usage: Include in SchemaObject SchemaFields as your_django_field = episodeProp()  
    schema.org description:An episode of a tv, radio or game media within a series or season. Supersedes episodes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Episode"""

    _prop_schema = 'episode'
    _expected_schema = 'Episode'
    _enum = False
    _format_as = "ForeignKey"


class numberOfPlayersProp(SchemaProperty):

    """
    SchemaField for numberOfPlayers
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfPlayersProp()  
    schema.org description:Indicate how many people can play this game (minimum, maximum, or range).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'numberOfPlayers'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class productionCompanyProp(SchemaProperty):

    """
    SchemaField for productionCompany
    Usage: Include in SchemaObject SchemaFields as your_django_field = productionCompanyProp()  
    schema.org description:The production company or studio responsible for the item e.g. series, video game, episode etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'productionCompany'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class gameItemProp(SchemaProperty):

    """
    SchemaField for gameItem
    Usage: Include in SchemaObject SchemaFields as your_django_field = gameItemProp()  
    schema.org description:An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'gameItem'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class musicByProp(SchemaProperty):

    """
    SchemaField for musicBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicByProp()  
    schema.org description:The composer of the soundtrack.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicGroup"""

    _prop_schema = 'musicBy'
    _expected_schema = 'MusicGroup'
    _enum = False
    _format_as = "ForeignKey"


class actorProp(SchemaProperty):

    """
    SchemaField for actor
    Usage: Include in SchemaObject SchemaFields as your_django_field = actorProp()  
    schema.org description:An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.

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
    schema.org description:A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'director'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class questProp(SchemaProperty):

    """
    SchemaField for quest
    Usage: Include in SchemaObject SchemaFields as your_django_field = questProp()  
    schema.org description:The task that a player-controlled character, or group of characters may complete in order to gain a reward.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'quest'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class characterAttributeProp(SchemaProperty):

    """
    SchemaField for characterAttribute
    Usage: Include in SchemaObject SchemaFields as your_django_field = characterAttributeProp()  
    schema.org description:A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'characterAttribute'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class numberOfEpisodesProp(SchemaProperty):

    """
    SchemaField for numberOfEpisodes
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfEpisodesProp()  
    schema.org description:The number of episodes in this season or series.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'numberOfEpisodes'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


class gameLocationProp(SchemaProperty):

    """
    SchemaField for gameLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = gameLocationProp()  
    schema.org description:Real or fictional location of the game (or part of game).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'gameLocation'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class numberOfSeasonsProp(SchemaProperty):

    """
    SchemaField for numberOfSeasons
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfSeasonsProp()  
    schema.org description:The number of seasons in this series.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'numberOfSeasons'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


class playModeProp(SchemaProperty):

    """
    SchemaField for playMode
    Usage: Include in SchemaObject SchemaFields as your_django_field = playModeProp()  
    schema.org description:Indicates whether this game is multi-player, co-op or single-player. The game can be marked as multi-player, co-op and single-player at the same time.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference GamePlayMode"""

    _prop_schema = 'playMode'
    _expected_schema = 'GamePlayMode'
    _enum = False
    _format_as = "ForeignKey"


class trailerProp(SchemaProperty):

    """
    SchemaField for trailer
    Usage: Include in SchemaObject SchemaFields as your_django_field = trailerProp()  
    schema.org description:The trailer of a movie or tv/radio series, season, episode, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference VideoObject"""

    _prop_schema = 'trailer'
    _expected_schema = 'VideoObject'
    _enum = False
    _format_as = "ForeignKey"


class gamePlatformProp(SchemaProperty):

    """
    SchemaField for gamePlatform
    Usage: Include in SchemaObject SchemaFields as your_django_field = gamePlatformProp()  
    schema.org description:The electronic systems used to play video games.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gamePlatform'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
