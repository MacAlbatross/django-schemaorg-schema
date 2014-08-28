# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MediaObjectSchema(SchemaObject):

    """Schema Mixin for MediaObject
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An image, video, or audio object embedded in a web page. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject&#39;s).
    """

    def __init__(self):
        self.schema = 'MediaObject'


class contentUrlProp(SchemaProperty):

    """
    SchemaField for contentUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = contentUrlProp()
    schema.org description:Actual bytes of the media object, for example the image file or video file. (previous spelling: contentURL)

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'contentUrl'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class uploadDateProp(SchemaProperty):

    """
    SchemaField for uploadDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = uploadDateProp()
    schema.org description:Date when this media object was uploaded to this site.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'uploadDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class playerTypeProp(SchemaProperty):

    """
    SchemaField for playerType
    Usage: Include in SchemaObject SchemaFields as your_django_field = playerTypeProp()
    schema.org description:Player type required-for example, Flash or Silverlight.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'playerType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class encodesCreativeWorkProp(SchemaProperty):

    """
    SchemaField for encodesCreativeWork
    Usage: Include in SchemaObject SchemaFields as your_django_field = encodesCreativeWorkProp()
    schema.org description:The creative work encoded by this media object

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference CreativeWork"""

    _prop_schema = 'encodesCreativeWork'
    _expected_schema = 'CreativeWork'
    _enum = False
    _format_as = "ForeignKey"


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


class expiresProp(SchemaProperty):

    """
    SchemaField for expires
    Usage: Include in SchemaObject SchemaFields as your_django_field = expiresProp()
    schema.org description:Date the content expires and is no longer useful or available. Useful for videos.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'expires'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class interactionCountProp(SchemaProperty):

    """
    SchemaField for interactionCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = interactionCountProp()
    schema.org description:A count of a specific user interactions with this item-for example, 20 UserLikes, 5 UserComments, or 300 UserDownloads. The user interaction type should be one of the sub types of UserInteraction.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'interactionCount'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class heightProp(SchemaProperty):

    """
    SchemaField for height
    Usage: Include in SchemaObject SchemaFields as your_django_field = heightProp()
    schema.org description:The height of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Distance"""

    _prop_schema = 'height'
    _expected_schema = 'Distance'
    _enum = False
    _format_as = "ForeignKey"


class encodingFormatProp(SchemaProperty):

    """
    SchemaField for encodingFormat
    Usage: Include in SchemaObject SchemaFields as your_django_field = encodingFormatProp()
    schema.org description:mp3, mpeg4, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'encodingFormat'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class associatedArticleProp(SchemaProperty):

    """
    SchemaField for associatedArticle
    Usage: Include in SchemaObject SchemaFields as your_django_field = associatedArticleProp()
    schema.org description:A NewsArticle associated with the Media Object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference NewsArticle"""

    _prop_schema = 'associatedArticle'
    _expected_schema = 'NewsArticle'
    _enum = False
    _format_as = "ForeignKey"


class offersProp(SchemaProperty):

    """
    SchemaField for offers
    Usage: Include in SchemaObject SchemaFields as your_django_field = offersProp()
    schema.org description:An offer to provide this item-for example, an offer to sell a product, rent the DVD of a movie, or give away tickets to an event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Offer"""

    _prop_schema = 'offers'
    _expected_schema = 'Offer'
    _enum = False
    _format_as = "ForeignKey"


class publicationProp(SchemaProperty):

    """
    SchemaField for publication
    Usage: Include in SchemaObject SchemaFields as your_django_field = publicationProp()
    schema.org description:A publication event associated with the episode, clip or media object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PublicationEvent"""

    _prop_schema = 'publication'
    _expected_schema = 'PublicationEvent'
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


class requiresSubscriptionProp(SchemaProperty):

    """
    SchemaField for requiresSubscription
    Usage: Include in SchemaObject SchemaFields as your_django_field = requiresSubscriptionProp()
    schema.org description:Indicates if use of the media require a subscription (either paid or free). Allowed values are true or false (note that an earlier version had &#39;yes&#39;, &#39;no&#39;).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'requiresSubscription'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


class embedUrlProp(SchemaProperty):

    """
    SchemaField for embedUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = embedUrlProp()
    schema.org description:A URL pointing to a player for a specific video. In general, this is the information in the src element of an embed tag and should not be the same as the content of the loc tag. (previous spelling: embedURL)

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'embedUrl'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class regionsAllowedProp(SchemaProperty):

    """
    SchemaField for regionsAllowed
    Usage: Include in SchemaObject SchemaFields as your_django_field = regionsAllowedProp()
    schema.org description:The regions where the media is allowed. If not specified, then it&#39;s assumed to be allowed everywhere. Specify the countries in ISO 3166 format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'regionsAllowed'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class bitrateProp(SchemaProperty):

    """
    SchemaField for bitrate
    Usage: Include in SchemaObject SchemaFields as your_django_field = bitrateProp()
    schema.org description:The bitrate of the media object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'bitrate'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class widthProp(SchemaProperty):

    """
    SchemaField for width
    Usage: Include in SchemaObject SchemaFields as your_django_field = widthProp()
    schema.org description:The width of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Distance"""

    _prop_schema = 'width'
    _expected_schema = 'Distance'
    _enum = False
    _format_as = "ForeignKey"


class contentSizeProp(SchemaProperty):

    """
    SchemaField for contentSize
    Usage: Include in SchemaObject SchemaFields as your_django_field = contentSizeProp()
    schema.org description:File size in (mega/kilo) bytes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'contentSize'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
