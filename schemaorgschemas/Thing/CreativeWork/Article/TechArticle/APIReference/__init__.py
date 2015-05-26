# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.CreativeWork.Article import articleBodyProp, paginationProp, wordCountProp, pageEndProp, articleSectionProp, pageStartProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing.CreativeWork.Article.TechArticle import proficiencyLevelProp, dependenciesProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class APIReferenceSchema(SchemaObject):

    """Schema Mixin for APIReference
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Reference documentation for application programming interfaces (APIs).
    """

    def __init__(self):
        self.schema = 'APIReference'


class targetPlatformProp(SchemaProperty):

    """
    SchemaField for targetPlatform
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetPlatformProp()  
    schema.org description:Type of app development: phone, Metro style, desktop, XBox, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'targetPlatform'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class executableLibraryNameProp(SchemaProperty):

    """
    SchemaField for executableLibraryName
    Usage: Include in SchemaObject SchemaFields as your_django_field = executableLibraryNameProp()  
    schema.org description:Library file name e.g., mscorlib.dll, system.web.dll. Supersedes assembly.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'executableLibraryName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class programmingModelProp(SchemaProperty):

    """
    SchemaField for programmingModel
    Usage: Include in SchemaObject SchemaFields as your_django_field = programmingModelProp()  
    schema.org description:Indicates whether API is managed or unmanaged.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'programmingModel'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class assemblyVersionProp(SchemaProperty):

    """
    SchemaField for assemblyVersion
    Usage: Include in SchemaObject SchemaFields as your_django_field = assemblyVersionProp()  
    schema.org description:Associated product/technology version. e.g., .NET Framework 4.5.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'assemblyVersion'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
