# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicRecordingSchema(SchemaObject):

    """Schema Mixin for MusicRecording
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A music recording (track), usually a single song.
    """

    def __init__(self):
        self.schema = 'MusicRecording'


class recordingOfProp(SchemaProperty):

    """
    SchemaField for recordingOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = recordingOfProp()  
    schema.org description:The composition this track is a recording of. Inverse property: recordedAs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicComposition"""

    _prop_schema = 'recordingOf'
    _expected_schema = 'MusicComposition'
    _enum = False
    _format_as = "ForeignKey"


class inAlbumProp(SchemaProperty):

    """
    SchemaField for inAlbum
    Usage: Include in SchemaObject SchemaFields as your_django_field = inAlbumProp()  
    schema.org description:The album to which this recording belongs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicAlbum"""

    _prop_schema = 'inAlbum'
    _expected_schema = 'MusicAlbum'
    _enum = False
    _format_as = "ForeignKey"


class durationProp(SchemaProperty):

    """
    SchemaField for duration
    Usage: Include in SchemaObject SchemaFields as your_django_field = durationProp()  
    schema.org description:The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'duration'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class inPlaylistProp(SchemaProperty):

    """
    SchemaField for inPlaylist
    Usage: Include in SchemaObject SchemaFields as your_django_field = inPlaylistProp()  
    schema.org description:The playlist to which this recording belongs.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicPlaylist"""

    _prop_schema = 'inPlaylist'
    _expected_schema = 'MusicPlaylist'
    _enum = False
    _format_as = "ForeignKey"


class byArtistProp(SchemaProperty):

    """
    SchemaField for byArtist
    Usage: Include in SchemaObject SchemaFields as your_django_field = byArtistProp()  
    schema.org description:The artist that performed this album or recording.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicGroup"""

    _prop_schema = 'byArtist'
    _expected_schema = 'MusicGroup'
    _enum = False
    _format_as = "ForeignKey"


class isrcCodeProp(SchemaProperty):

    """
    SchemaField for isrcCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = isrcCodeProp()  
    schema.org description:The International Standard Recording Code for the recording.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isrcCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
