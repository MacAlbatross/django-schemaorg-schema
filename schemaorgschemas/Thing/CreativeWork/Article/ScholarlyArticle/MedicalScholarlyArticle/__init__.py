# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.Article import articleBodyProp, wordCountProp, articleSectionProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalScholarlyArticleSchema(SchemaObject):

    """Schema Mixin for MedicalScholarlyArticle
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A scholarly article in the medical domain.
    """

    def __init__(self):
        self.schema = 'MedicalScholarlyArticle'


class publicationTypeProp(SchemaProperty):

    """
    SchemaField for publicationType
    Usage: Include in SchemaObject SchemaFields as your_django_field = publicationTypeProp()  
    schema.org description:The type of the medical article, taken from the US NLM MeSH publication type catalog.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'publicationType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
