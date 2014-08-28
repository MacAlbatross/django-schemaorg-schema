# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ArticleSchema(SchemaObject):

    """Schema Mixin for Article
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.
    """

    def __init__(self):
        self.schema = 'Article'


class articleBodyProp(SchemaProperty):

    """
    SchemaField for articleBody
    Usage: Include in SchemaObject SchemaFields as your_django_field = articleBodyProp()
    schema.org description:The actual body of the article.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'articleBody'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class wordCountProp(SchemaProperty):

    """
    SchemaField for wordCount
    Usage: Include in SchemaObject SchemaFields as your_django_field = wordCountProp()
    schema.org description:The number of words in the text of the Article.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'wordCount'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


class articleSectionProp(SchemaProperty):

    """
    SchemaField for articleSection
    Usage: Include in SchemaObject SchemaFields as your_django_field = articleSectionProp()
    schema.org description:Articles may belong to one or more &#39;sections&#39; in a magazine or newspaper, such as Sports, Lifestyle, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'articleSection'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
