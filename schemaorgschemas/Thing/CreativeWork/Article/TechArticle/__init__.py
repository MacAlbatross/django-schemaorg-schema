# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.Article import articleBodyProp, paginationProp, wordCountProp, pageEndProp, articleSectionProp, pageStartProp
from schemaorgschemas.Thing.CreativeWork import educationalUseProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, aggregateRatingProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, associatedMediaProp, workExampleProp, sourceOrganizationProp, commentProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TechArticleSchema(SchemaObject):

    """Schema Mixin for TechArticle
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.
    """

    def __init__(self):
        self.schema = 'TechArticle'


class proficiencyLevelProp(SchemaProperty):

    """
    SchemaField for proficiencyLevel
    Usage: Include in SchemaObject SchemaFields as your_django_field = proficiencyLevelProp()  
    schema.org description:Proficiency needed for this content; expected values: &#39;Beginner&#39;, &#39;Expert&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'proficiencyLevel'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class dependenciesProp(SchemaProperty):

    """
    SchemaField for dependencies
    Usage: Include in SchemaObject SchemaFields as your_django_field = dependenciesProp()  
    schema.org description:Prerequisites needed to fulfill steps in article.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dependencies'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
