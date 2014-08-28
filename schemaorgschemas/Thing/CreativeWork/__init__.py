# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CreativeWorkSchema(SchemaObject):

    """Schema Mixin for CreativeWork
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    """

    def __init__(self):
        self.schema = 'CreativeWork'


class commentProp(SchemaProperty):

    """
    SchemaField for comment
    Usage: Include in SchemaObject SchemaFields as your_django_field = commentProp()
    schema.org description:Comments, typically from users, on this CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference UserComments"""

    _prop_schema = 'comment'
    _expected_schema = 'UserComments'
    _enum = False
    _format_as = "ForeignKey"


class copyrightYearProp(SchemaProperty):

    """
    SchemaField for copyrightYear
    Usage: Include in SchemaObject SchemaFields as your_django_field = copyrightYearProp()
    schema.org description:The year during which the claimed copyright for the CreativeWork was first asserted.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'copyrightYear'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class versionProp(SchemaProperty):

    """
    SchemaField for version
    Usage: Include in SchemaObject SchemaFields as your_django_field = versionProp()
    schema.org description:The version of the CreativeWork embodied by a specified resource.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'version'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class creatorProp(SchemaProperty):

    """
    SchemaField for creator
    Usage: Include in SchemaObject SchemaFields as your_django_field = creatorProp()
    schema.org description:The creator/author of this CreativeWork or UserComments. This is the same as the Author property for CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'creator'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class textProp(SchemaProperty):

    """
    SchemaField for text
    Usage: Include in SchemaObject SchemaFields as your_django_field = textProp()
    schema.org description:The textual content of this CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'text'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class citationProp(SchemaProperty):

    """
    SchemaField for citation
    Usage: Include in SchemaObject SchemaFields as your_django_field = citationProp()
    schema.org description:A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'citation'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class datePublishedProp(SchemaProperty):

    """
    SchemaField for datePublished
    Usage: Include in SchemaObject SchemaFields as your_django_field = datePublishedProp()
    schema.org description:Date of first broadcast/publication.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'datePublished'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class commentCountProp(SchemaProperty):

    """
    SchemaField for commentCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = commentCountProp()
    schema.org description:The number of comments this CreativeWork (e.g. Article, Question or Answer) has received. This is most applicable to works published in Web sites with commenting system; additional comments may exist elsewhere.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'commentCount'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class associatedMediaProp(SchemaProperty):

    """
    SchemaField for associatedMedia
    Usage: Include in SchemaObject SchemaFields as your_django_field = associatedMediaProp()
    schema.org description:The media objects that encode this creative work. This property is a synonym for encodings.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MediaObject"""

    _prop_schema = 'associatedMedia'
    _expected_schema = 'MediaObject'
    _enum = False
    _format_as = "ForeignKey"


class alternativeHeadlineProp(SchemaProperty):

    """
    SchemaField for alternativeHeadline
    Usage: Include in SchemaObject SchemaFields as your_django_field = alternativeHeadlineProp()
    schema.org description:A secondary title of the CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'alternativeHeadline'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class accountablePersonProp(SchemaProperty):

    """
    SchemaField for accountablePerson
    Usage: Include in SchemaObject SchemaFields as your_django_field = accountablePersonProp()
    schema.org description:Specifies the Person that is legally accountable for the CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'accountablePerson'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class videoProp(SchemaProperty):

    """
    SchemaField for video
    Usage: Include in SchemaObject SchemaFields as your_django_field = videoProp()
    schema.org description:An embedded video object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference VideoObject"""

    _prop_schema = 'video'
    _expected_schema = 'VideoObject'
    _enum = False
    _format_as = "ForeignKey"


class typicalAgeRangeProp(SchemaProperty):

    """
    SchemaField for typicalAgeRange
    Usage: Include in SchemaObject SchemaFields as your_django_field = typicalAgeRangeProp()
    schema.org description:The typical expected age range, e.g. &#39;7-9&#39;, &#39;11-&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'typicalAgeRange'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class contributorProp(SchemaProperty):

    """
    SchemaField for contributor
    Usage: Include in SchemaObject SchemaFields as your_django_field = contributorProp()
    schema.org description:A secondary contributor to the CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'contributor'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class thumbnailUrlProp(SchemaProperty):

    """
    SchemaField for thumbnailUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = thumbnailUrlProp()
    schema.org description:A thumbnail image relevant to the Thing.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'thumbnailUrl'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class accessibilityFeatureProp(SchemaProperty):

    """
    SchemaField for accessibilityFeature
    Usage: Include in SchemaObject SchemaFields as your_django_field = accessibilityFeatureProp()
    schema.org description:Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility (WebSchemas wiki lists possible values).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'accessibilityFeature'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class interactivityTypeProp(SchemaProperty):

    """
    SchemaField for interactivityType
    Usage: Include in SchemaObject SchemaFields as your_django_field = interactivityTypeProp()
    schema.org description:The predominant mode of learning supported by the learning resource. Acceptable values are &#39;active&#39;, &#39;expositive&#39;, or &#39;mixed&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'interactivityType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class discussionUrlProp(SchemaProperty):

    """
    SchemaField for discussionUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = discussionUrlProp()
    schema.org description:A link to the page containing the comments of the CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'discussionUrl'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class authorProp(SchemaProperty):

    """
    SchemaField for author
    Usage: Include in SchemaObject SchemaFields as your_django_field = authorProp()
    schema.org description:The author of this content. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'author'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class headlineProp(SchemaProperty):

    """
    SchemaField for headline
    Usage: Include in SchemaObject SchemaFields as your_django_field = headlineProp()
    schema.org description:Headline of the article

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'headline'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class reviewProp(SchemaProperty):

    """
    SchemaField for review
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewProp()
    schema.org description:A review of the item. Supercedes reviews.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Review"""

    _prop_schema = 'review'
    _expected_schema = 'Review'
    _enum = False
    _format_as = "ForeignKey"


class encodingProp(SchemaProperty):

    """
    SchemaField for encoding
    Usage: Include in SchemaObject SchemaFields as your_django_field = encodingProp()
    schema.org description:A media object that encode this CreativeWork. Supercedes encodings.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MediaObject"""

    _prop_schema = 'encoding'
    _expected_schema = 'MediaObject'
    _enum = False
    _format_as = "ForeignKey"


class contentRatingProp(SchemaProperty):

    """
    SchemaField for contentRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = contentRatingProp()
    schema.org description:Official rating of a piece of content-for example,&#39;MPAA PG-13&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'contentRating'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class editorProp(SchemaProperty):

    """
    SchemaField for editor
    Usage: Include in SchemaObject SchemaFields as your_django_field = editorProp()
    schema.org description:Specifies the Person who edited the CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'editor'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class providerProp(SchemaProperty):

    """
    SchemaField for provider
    Usage: Include in SchemaObject SchemaFields as your_django_field = providerProp()
    schema.org description:The organization or agency that is providing the service.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'provider'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class publishingPrinciplesProp(SchemaProperty):

    """
    SchemaField for publishingPrinciples
    Usage: Include in SchemaObject SchemaFields as your_django_field = publishingPrinciplesProp()
    schema.org description:Link to page describing the editorial principles of the organization primarily responsible for the creation of the CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'publishingPrinciples'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class accessibilityHazardProp(SchemaProperty):

    """
    SchemaField for accessibilityHazard
    Usage: Include in SchemaObject SchemaFields as your_django_field = accessibilityHazardProp()
    schema.org description:A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3. (WebSchemas wiki lists possible values)

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'accessibilityHazard'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class dateModifiedProp(SchemaProperty):

    """
    SchemaField for dateModified
    Usage: Include in SchemaObject SchemaFields as your_django_field = dateModifiedProp()
    schema.org description:The date on which the CreativeWork was most recently modified.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dateModified'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class timeRequiredProp(SchemaProperty):

    """
    SchemaField for timeRequired
    Usage: Include in SchemaObject SchemaFields as your_django_field = timeRequiredProp()
    schema.org description:Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience, e.g. &#39;P30M&#39;, &#39;P1H25M&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'timeRequired'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class educationalAlignmentProp(SchemaProperty):

    """
    SchemaField for educationalAlignment
    Usage: Include in SchemaObject SchemaFields as your_django_field = educationalAlignmentProp()
    schema.org description:An alignment to an established educational framework.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AlignmentObject"""

    _prop_schema = 'educationalAlignment'
    _expected_schema = 'AlignmentObject'
    _enum = False
    _format_as = "ForeignKey"


class awardProp(SchemaProperty):

    """
    SchemaField for award
    Usage: Include in SchemaObject SchemaFields as your_django_field = awardProp()
    schema.org description:An award won by this person or for this creative work. Supercedes awards.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'award'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class dateCreatedProp(SchemaProperty):

    """
    SchemaField for dateCreated
    Usage: Include in SchemaObject SchemaFields as your_django_field = dateCreatedProp()
    schema.org description:The date on which the CreativeWork was created.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dateCreated'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class copyrightHolderProp(SchemaProperty):

    """
    SchemaField for copyrightHolder
    Usage: Include in SchemaObject SchemaFields as your_django_field = copyrightHolderProp()
    schema.org description:The party holding the legal copyright to the CreativeWork.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'copyrightHolder'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class audienceProp(SchemaProperty):

    """
    SchemaField for audience
    Usage: Include in SchemaObject SchemaFields as your_django_field = audienceProp()
    schema.org description:The intended audience of the item, i.e. the group for whom the item was created.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Audience"""

    _prop_schema = 'audience'
    _expected_schema = 'Audience'
    _enum = False
    _format_as = "ForeignKey"


class genreProp(SchemaProperty):

    """
    SchemaField for genre
    Usage: Include in SchemaObject SchemaFields as your_django_field = genreProp()
    schema.org description:Genre of the creative work

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'genre'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class contentLocationProp(SchemaProperty):

    """
    SchemaField for contentLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = contentLocationProp()
    schema.org description:The location of the content.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'contentLocation'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"


class educationalUseProp(SchemaProperty):

    """
    SchemaField for educationalUse
    Usage: Include in SchemaObject SchemaFields as your_django_field = educationalUseProp()
    schema.org description:The purpose of a work in the context of education; for example, &#39;assignment&#39;, &#39;group work&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'educationalUse'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class accessibilityAPIProp(SchemaProperty):

    """
    SchemaField for accessibilityAPI
    Usage: Include in SchemaObject SchemaFields as your_django_field = accessibilityAPIProp()
    schema.org description:Indicates that the resource is compatible with the referenced accessibility API (WebSchemas wiki lists possible values).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'accessibilityAPI'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class publisherProp(SchemaProperty):

    """
    SchemaField for publisher
    Usage: Include in SchemaObject SchemaFields as your_django_field = publisherProp()
    schema.org description:The publisher of the creative work.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'publisher'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class aboutProp(SchemaProperty):

    """
    SchemaField for about
    Usage: Include in SchemaObject SchemaFields as your_django_field = aboutProp()
    schema.org description:The subject matter of the content.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'about'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class aggregateRatingProp(SchemaProperty):

    """
    SchemaField for aggregateRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = aggregateRatingProp()
    schema.org description:The overall rating, based on a collection of reviews or ratings, of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AggregateRating"""

    _prop_schema = 'aggregateRating'
    _expected_schema = 'AggregateRating'
    _enum = False
    _format_as = "ForeignKey"


class sourceOrganizationProp(SchemaProperty):

    """
    SchemaField for sourceOrganization
    Usage: Include in SchemaObject SchemaFields as your_django_field = sourceOrganizationProp()
    schema.org description:The Organization on whose behalf the creator was working.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'sourceOrganization'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class inLanguageProp(SchemaProperty):

    """
    SchemaField for inLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = inLanguageProp()
    schema.org description:The language of the content. please use one of the language codes from the IETF BCP 47 standard.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'inLanguage'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class isFamilyFriendlyProp(SchemaProperty):

    """
    SchemaField for isFamilyFriendly
    Usage: Include in SchemaObject SchemaFields as your_django_field = isFamilyFriendlyProp()
    schema.org description:Indicates whether this content is family friendly.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isFamilyFriendly'
    _expected_schema = None
    _enum = False
    _format_as = "BooleanField"


class learningResourceTypeProp(SchemaProperty):

    """
    SchemaField for learningResourceType
    Usage: Include in SchemaObject SchemaFields as your_django_field = learningResourceTypeProp()
    schema.org description:The predominant type or kind characterizing the learning resource. For example, &#39;presentation&#39;, &#39;handout&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'learningResourceType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class accessibilityControlProp(SchemaProperty):

    """
    SchemaField for accessibilityControl
    Usage: Include in SchemaObject SchemaFields as your_django_field = accessibilityControlProp()
    schema.org description:Identifies input methods that are sufficient to fully control the described resource (WebSchemas wiki lists possible values).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'accessibilityControl'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class keywordsProp(SchemaProperty):

    """
    SchemaField for keywords
    Usage: Include in SchemaObject SchemaFields as your_django_field = keywordsProp()
    schema.org description:The keywords/tags used to describe this content.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'keywords'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class mentionsProp(SchemaProperty):

    """
    SchemaField for mentions
    Usage: Include in SchemaObject SchemaFields as your_django_field = mentionsProp()
    schema.org description:Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'mentions'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class audioProp(SchemaProperty):

    """
    SchemaField for audio
    Usage: Include in SchemaObject SchemaFields as your_django_field = audioProp()
    schema.org description:An embedded audio object.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AudioObject"""

    _prop_schema = 'audio'
    _expected_schema = 'AudioObject'
    _enum = False
    _format_as = "ForeignKey"


class isBasedOnUrlProp(SchemaProperty):

    """
    SchemaField for isBasedOnUrl
    Usage: Include in SchemaObject SchemaFields as your_django_field = isBasedOnUrlProp()
    schema.org description:A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isBasedOnUrl'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"
