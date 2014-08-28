# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class QuestionSchema(SchemaObject):

    """Schema Mixin for Question
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.
    """

    def __init__(self):
        self.schema = 'Question'


class answerCountProp(SchemaProperty):

    """
    SchemaField for answerCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = answerCountProp()
    schema.org description:The number of answers this question has received.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'answerCount'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


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


class suggestedAnswerProp(SchemaProperty):

    """
    SchemaField for suggestedAnswer
    Usage: Include in SchemaObject SchemaFields as your_django_field = suggestedAnswerProp()
    schema.org description:An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site, often collected in a QAPage.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Answer"""

    _prop_schema = 'suggestedAnswer'
    _expected_schema = 'Answer'
    _enum = False
    _format_as = "ForeignKey"


class acceptedAnswerProp(SchemaProperty):

    """
    SchemaField for acceptedAnswer
    Usage: Include in SchemaObject SchemaFields as your_django_field = acceptedAnswerProp()
    schema.org description:The answer that has been accepted as best, typically on a Question/Answer site. Sites vary in their selection mechanisms, e.g. drawing on community opinion and/or the view of the Question author.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Answer"""

    _prop_schema = 'acceptedAnswer'
    _expected_schema = 'Answer'
    _enum = False
    _format_as = "ForeignKey"
