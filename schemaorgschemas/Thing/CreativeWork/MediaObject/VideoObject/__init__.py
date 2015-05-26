# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork.MediaObject import contentUrlProp, playerTypeProp, encodesCreativeWorkProp, productionCompanyProp, expiresProp, heightProp, encodingFormatProp, associatedArticleProp, requiresSubscriptionProp, uploadDateProp, durationProp, embedUrlProp, regionsAllowedProp, bitrateProp, widthProp, contentSizeProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VideoObjectSchema(SchemaObject):

    """Schema Mixin for VideoObject
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A video file.
    """

    def __init__(self):
        self.schema = 'VideoObject'


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


class captionProp(SchemaProperty):

    """
    SchemaField for caption
    Usage: Include in SchemaObject SchemaFields as your_django_field = captionProp()  
    schema.org description:The caption for this object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'caption'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class videoQualityProp(SchemaProperty):

    """
    SchemaField for videoQuality
    Usage: Include in SchemaObject SchemaFields as your_django_field = videoQualityProp()  
    schema.org description:The quality of the video.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'videoQuality'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class videoFrameSizeProp(SchemaProperty):

    """
    SchemaField for videoFrameSize
    Usage: Include in SchemaObject SchemaFields as your_django_field = videoFrameSizeProp()  
    schema.org description:The frame size of the video.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'videoFrameSize'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class transcriptProp(SchemaProperty):

    """
    SchemaField for transcript
    Usage: Include in SchemaObject SchemaFields as your_django_field = transcriptProp()  
    schema.org description:If this MediaObject is an AudioObject or VideoObject, the transcript of that object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'transcript'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class thumbnailProp(SchemaProperty):

    """
    SchemaField for thumbnail
    Usage: Include in SchemaObject SchemaFields as your_django_field = thumbnailProp()  
    schema.org description:Thumbnail image for an image or video.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'thumbnail'
    _expected_schema = 'ImageObject'
    _enum = False
    _format_as = "URLField"


# schema.org version 2.0
