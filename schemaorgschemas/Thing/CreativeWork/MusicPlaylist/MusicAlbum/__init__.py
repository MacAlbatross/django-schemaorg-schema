# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork.MusicPlaylist import trackProp, numTracksProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, aggregateRatingProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, associatedMediaProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicAlbumSchema(SchemaObject):

    """Schema Mixin for MusicAlbum
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A collection of music tracks.
    """

    def __init__(self):
        self.schema = 'MusicAlbum'


class albumReleaseProp(SchemaProperty):

    """
    SchemaField for albumRelease
    Usage: Include in SchemaObject SchemaFields as your_django_field = albumReleaseProp()  
    schema.org description:A release of this album. Inverse property: releaseOf.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicRelease"""

    _prop_schema = 'albumRelease'
    _expected_schema = 'MusicRelease'
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


class albumProductionTypeProp(SchemaProperty):

    """
    SchemaField for albumProductionType
    Usage: Include in SchemaObject SchemaFields as your_django_field = albumProductionTypeProp()  
    schema.org description:Classification of the album by it&#39;s type of content: soundtrack, live album, studio album, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicAlbumProductionType"""

    _prop_schema = 'albumProductionType'
    _expected_schema = 'MusicAlbumProductionType'
    _enum = False
    _format_as = "ForeignKey"


class albumReleaseTypeProp(SchemaProperty):

    """
    SchemaField for albumReleaseType
    Usage: Include in SchemaObject SchemaFields as your_django_field = albumReleaseTypeProp()  
    schema.org description:The kind of release which this album is: single, EP or album.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicAlbumReleaseType"""

    _prop_schema = 'albumReleaseType'
    _expected_schema = 'MusicAlbumReleaseType'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
