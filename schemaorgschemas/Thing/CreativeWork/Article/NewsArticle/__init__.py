# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.Article import articleBodyProp, paginationProp, wordCountProp, pageEndProp, articleSectionProp, pageStartProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, aggregateRatingProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, associatedMediaProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NewsArticleSchema(SchemaObject):

    """Schema Mixin for NewsArticle
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A news article.
    """

    def __init__(self):
        self.schema = 'NewsArticle'


class printEditionProp(SchemaProperty):

    """
    SchemaField for printEdition
    Usage: Include in SchemaObject SchemaFields as your_django_field = printEditionProp()  
    schema.org description:The edition of the print product in which the NewsArticle appears.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'printEdition'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class datelineProp(SchemaProperty):

    """
    SchemaField for dateline
    Usage: Include in SchemaObject SchemaFields as your_django_field = datelineProp()  
    schema.org description:The location where the NewsArticle was produced.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dateline'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class printColumnProp(SchemaProperty):

    """
    SchemaField for printColumn
    Usage: Include in SchemaObject SchemaFields as your_django_field = printColumnProp()  
    schema.org description:The number of the column in which the NewsArticle appears in the print edition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'printColumn'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class printPageProp(SchemaProperty):

    """
    SchemaField for printPage
    Usage: Include in SchemaObject SchemaFields as your_django_field = printPageProp()  
    schema.org description:If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'printPage'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class printSectionProp(SchemaProperty):

    """
    SchemaField for printSection
    Usage: Include in SchemaObject SchemaFields as your_django_field = printSectionProp()  
    schema.org description:If this NewsArticle appears in print, this field indicates the print section in which the article appeared.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'printSection'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
