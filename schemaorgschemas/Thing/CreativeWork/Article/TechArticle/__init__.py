# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.Article import articleBodyProp, wordCountProp, articleSectionProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

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
