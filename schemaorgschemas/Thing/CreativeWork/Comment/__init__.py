# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CommentSchema(SchemaObject):

    """Schema Mixin for Comment
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A comment on an item - for example, a comment on a blog post. The comment&#39;s content is expressed via the &quot;text&quot; property, and its topic via &quot;about&quot;, properties shared with all CreativeWorks.
    """

    def __init__(self):
        self.schema = 'Comment'


class downvoteCountProp(SchemaProperty):

    """
    SchemaField for downvoteCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = downvoteCountProp()  
    schema.org description:The number of downvotes this question has received from the community.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'downvoteCount'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class upvoteCountProp(SchemaProperty):

    """
    SchemaField for upvoteCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = upvoteCountProp()  
    schema.org description:The number of upvotes this question has received from the community.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'upvoteCount'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class parentItemProp(SchemaProperty):

    """
    SchemaField for parentItem
    Usage: Include in SchemaObject SchemaFields as your_django_field = parentItemProp()  
    schema.org description:The parent of a question, answer or item in general.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Question"""

    _prop_schema = 'parentItem'
    _expected_schema = 'Question'
    _enum = False
    _format_as = "ForeignKey"
