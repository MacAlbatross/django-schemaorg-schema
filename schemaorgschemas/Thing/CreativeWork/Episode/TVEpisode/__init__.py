# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.Episode import episodeNumberProp, productionCompanyProp, partOfSeasonProp, musicByProp, actorProp, directorProp, partOfSeriesProp, trailerProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TVEpisodeSchema(SchemaObject):

    """Schema Mixin for TVEpisode
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A TV episode which can be part of a series or season.
    """

    def __init__(self):
        self.schema = 'TVEpisode'


class subtitleLanguageProp(SchemaProperty):

    """
    SchemaField for subtitleLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = subtitleLanguageProp()  
    schema.org description:Languages in which subtitles/captions are available, in IETF BCP 47 standard format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'subtitleLanguage'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
