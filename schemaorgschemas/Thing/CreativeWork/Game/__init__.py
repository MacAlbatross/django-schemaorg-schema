# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GameSchema(SchemaObject):

    """Schema Mixin for Game
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting. See also open issues list.
    """

    def __init__(self):
        self.schema = 'Game'


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


class gameLocationProp(SchemaProperty):

    """
    SchemaField for gameLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = gameLocationProp()  
    schema.org description:Real or fictional location of the game (or part of game).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'gameLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
