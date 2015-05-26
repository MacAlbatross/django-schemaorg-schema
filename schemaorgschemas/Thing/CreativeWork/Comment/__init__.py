# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

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
    schema.org description:The number of downvotes this question, answer or comment has received from the community.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'downvoteCount'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


class upvoteCountProp(SchemaProperty):

    """
    SchemaField for upvoteCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = upvoteCountProp()  
    schema.org description:The number of upvotes this question, answer or comment has received from the community.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'upvoteCount'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


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


# schema.org version 2.0
