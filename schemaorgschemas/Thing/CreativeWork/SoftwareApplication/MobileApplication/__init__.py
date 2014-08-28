# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing.CreativeWork.SoftwareApplication import countriesNotSupportedProp, screenshotProp, installUrlProp, operatingSystemProp, processorRequirementsProp, releaseNotesProp, softwareVersionProp, memoryRequirementsProp, downloadUrlProp, applicationCategoryProp, countriesSupportedProp, storageRequirementsProp, featureListProp, deviceProp, requirementsProp, applicationSubCategoryProp, permissionsProp, fileFormatProp, applicationSuiteProp, fileSizeProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MobileApplicationSchema(SchemaObject):

    """Schema Mixin for MobileApplication
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A mobile software application.
    """

    def __init__(self):
        self.schema = 'MobileApplication'


class carrierRequirementsProp(SchemaProperty):

    """
    SchemaField for carrierRequirements
    Usage: Include in SchemaObject SchemaFields as your_django_field = carrierRequirementsProp()  
    schema.org description:Specifies specific carrier(s) requirements for the application (e.g. an application may only work on a specific carrier network).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'carrierRequirements'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
