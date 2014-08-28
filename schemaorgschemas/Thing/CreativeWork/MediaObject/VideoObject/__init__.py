# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork.MediaObject import contentUrlProp, uploadDateProp, playerTypeProp, encodesCreativeWorkProp, productionCompanyProp, expiresProp, interactionCountProp, heightProp, encodingFormatProp, associatedArticleProp, offersProp, publicationProp, durationProp, requiresSubscriptionProp, embedUrlProp, regionsAllowedProp, bitrateProp, widthProp, contentSizeProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VideoObjectSchema(SchemaObject):

    """Schema Mixin for VideoObject
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A video file.
    """

    def __init__(self):
        self.schema = 'VideoObject'


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


class productionCompanyProp(SchemaProperty):

    """
    SchemaField for productionCompany
    Usage: Include in SchemaObject SchemaFields as your_django_field = productionCompanyProp()  
    schema.org description:The production company or studio that made the movie, tv/radio series, season, or episode, or media object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'productionCompany'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


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
