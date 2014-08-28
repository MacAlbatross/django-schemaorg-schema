# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork.MediaObject import contentUrlProp, uploadDateProp, playerTypeProp, encodesCreativeWorkProp, productionCompanyProp, expiresProp, interactionCountProp, heightProp, encodingFormatProp, associatedArticleProp, offersProp, publicationProp, durationProp, requiresSubscriptionProp, embedUrlProp, regionsAllowedProp, bitrateProp, widthProp, contentSizeProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AudioObjectSchema(SchemaObject):

    """Schema Mixin for AudioObject
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An audio file.
    """

    def __init__(self):
        self.schema = 'AudioObject'


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
