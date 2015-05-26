# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing.CreativeWork.SoftwareApplication import installUrlProp, memoryRequirementsProp, processorRequirementsProp, countriesSupportedProp, featureListProp, availableOnDeviceProp, applicationSubCategoryProp, fileFormatProp, applicationSuiteProp, softwareHelpProp, countriesNotSupportedProp, applicationCategoryProp, softwareRequirementsProp, screenshotProp, releaseNotesProp, softwareAddOnProp, storageRequirementsProp, fileSizeProp, permissionsProp, downloadUrlProp, softwareVersionProp, operatingSystemProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class WebApplicationSchema(SchemaObject):

    """Schema Mixin for WebApplication
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Web applications.
    """

    def __init__(self):
        self.schema = 'WebApplication'


class browserRequirementsProp(SchemaProperty):

    """
    SchemaField for browserRequirements
    Usage: Include in SchemaObject SchemaFields as your_django_field = browserRequirementsProp()  
    schema.org description:Specifies browser requirements in human-readable text. For example,&quot;requires HTML5 support&quot;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'browserRequirements'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
