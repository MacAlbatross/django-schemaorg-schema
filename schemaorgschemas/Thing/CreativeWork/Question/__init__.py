# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, aggregateRatingProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, associatedMediaProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

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
    used to reference Integer"""

    _prop_schema = 'answerCount'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


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


class suggestedAnswerProp(SchemaProperty):

    """
    SchemaField for suggestedAnswer
    Usage: Include in SchemaObject SchemaFields as your_django_field = suggestedAnswerProp()  
    schema.org description:An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site.

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


# schema.org version 2.0
