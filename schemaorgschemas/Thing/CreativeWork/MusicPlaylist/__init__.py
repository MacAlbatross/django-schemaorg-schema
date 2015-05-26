# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicPlaylistSchema(SchemaObject):

    """Schema Mixin for MusicPlaylist
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A collection of music tracks in playlist form.
    """

    def __init__(self):
        self.schema = 'MusicPlaylist'


class trackProp(SchemaProperty):

    """
    SchemaField for track
    Usage: Include in SchemaObject SchemaFields as your_django_field = trackProp()  
    schema.org description:A music recording (track)usually a single song. If an ItemList is given, the list should contain items of type MusicRecording. Supersedes tracks.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicRecording"""

    _prop_schema = 'track'
    _expected_schema = 'MusicRecording'
    _enum = False
    _format_as = "ForeignKey"


class numTracksProp(SchemaProperty):

    """
    SchemaField for numTracks
    Usage: Include in SchemaObject SchemaFields as your_django_field = numTracksProp()  
    schema.org description:The number of tracks in this album or playlist.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'numTracks'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
