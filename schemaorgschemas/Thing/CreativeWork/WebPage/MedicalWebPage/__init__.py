# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.WebPage import mainContentOfPageProp, significantLinkProp, lastReviewedProp, specialtyProp, breadcrumbProp, reviewedByProp, isPartOfProp, primaryImageOfPageProp, relatedLinkProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalWebPageSchema(SchemaObject):

    """Schema Mixin for MedicalWebPage
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A web page that provides medical information.
    """

    def __init__(self):
        self.schema = 'MedicalWebPage'


class aspectProp(SchemaProperty):

    """
    SchemaField for aspect
    Usage: Include in SchemaObject SchemaFields as your_django_field = aspectProp()
    schema.org description:An aspect of medical practice that is considered on the page, such as &#39;diagnosis&#39;, &#39;treatment&#39;, &#39;causes&#39;, &#39;prognosis&#39;, &#39;etiology&#39;, &#39;epidemiology&#39;, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'aspect'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
