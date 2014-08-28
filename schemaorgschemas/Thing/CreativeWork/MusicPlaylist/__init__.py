# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

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
    schema.org description:A music recording (track)-usually a single song. Supercedes tracks.

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
    """

    _prop_schema = 'numTracks'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"
