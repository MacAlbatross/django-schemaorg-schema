# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork.MusicPlaylist import trackProp, numTracksProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicReleaseSchema(SchemaObject):

    """Schema Mixin for MusicRelease
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A MusicRelease is a specific release of a music album.
    """

    def __init__(self):
        self.schema = 'MusicRelease'


class musicReleaseFormatProp(SchemaProperty):

    """
    SchemaField for musicReleaseFormat
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicReleaseFormatProp()  
    schema.org description:Format of this release (the type of recording media used, ie. compact disc, digital media, LP, etc.).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicReleaseFormatType"""

    _prop_schema = 'musicReleaseFormat'
    _expected_schema = 'MusicReleaseFormatType'
    _enum = False
    _format_as = "ForeignKey"


class recordLabelProp(SchemaProperty):

    """
    SchemaField for recordLabel
    Usage: Include in SchemaObject SchemaFields as your_django_field = recordLabelProp()  
    schema.org description:The label that issued the release.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'recordLabel'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class catalogNumberProp(SchemaProperty):

    """
    SchemaField for catalogNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = catalogNumberProp()  
    schema.org description:The catalog number for the release.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'catalogNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class releaseOfProp(SchemaProperty):

    """
    SchemaField for releaseOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = releaseOfProp()  
    schema.org description:The album this is a release of. Inverse property: albumRelease.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicAlbum"""

    _prop_schema = 'releaseOf'
    _expected_schema = 'MusicAlbum'
    _enum = False
    _format_as = "ForeignKey"


class creditedToProp(SchemaProperty):

    """
    SchemaField for creditedTo
    Usage: Include in SchemaObject SchemaFields as your_django_field = creditedToProp()  
    schema.org description:The group the release is credited to if different than the byArtist. For example, Red and Blue is credited to &quot;Stefani Germanotta Band&quot;, but by Lady Gaga.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'creditedTo'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
