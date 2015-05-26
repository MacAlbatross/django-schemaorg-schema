# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork.Game import numberOfPlayersProp, questProp, gameItemProp, characterAttributeProp, gameLocationProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing.CreativeWork.SoftwareApplication import installUrlProp, memoryRequirementsProp, processorRequirementsProp, countriesSupportedProp, featureListProp, availableOnDeviceProp, applicationSubCategoryProp, fileFormatProp, applicationSuiteProp, softwareHelpProp, countriesNotSupportedProp, applicationCategoryProp, softwareRequirementsProp, screenshotProp, releaseNotesProp, softwareAddOnProp, storageRequirementsProp, fileSizeProp, permissionsProp, downloadUrlProp, softwareVersionProp, operatingSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VideoGameSchema(SchemaObject):

    """Schema Mixin for VideoGame
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A video game is an electronic game that involves human interaction with a user interface to generate visual feedback on a video device.
    """

    def __init__(self):
        self.schema = 'VideoGame'


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


class gameTipProp(SchemaProperty):

    """
    SchemaField for gameTip
    Usage: Include in SchemaObject SchemaFields as your_django_field = gameTipProp()  
    schema.org description:Links to tips, tactics, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWork"""

    _prop_schema = 'gameTip'
    _expected_schema = 'CreativeWork'
    _enum = False
    _format_as = "ForeignKey"


class musicByProp(SchemaProperty):

    """
    SchemaField for musicBy
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicByProp()  
    schema.org description:The composer of the soundtrack.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'musicBy'
    _expected_schema = 'Person'
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


class gameServerProp(SchemaProperty):

    """
    SchemaField for gameServer
    Usage: Include in SchemaObject SchemaFields as your_django_field = gameServerProp()  
    schema.org description:The server on which it is possible to play the game. Inverse property: game.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference GameServer"""

    _prop_schema = 'gameServer'
    _expected_schema = 'GameServer'
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
