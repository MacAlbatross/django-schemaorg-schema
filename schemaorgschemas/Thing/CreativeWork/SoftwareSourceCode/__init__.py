# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, aggregateRatingProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, associatedMediaProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SoftwareSourceCodeSchema(SchemaObject):

    """Schema Mixin for SoftwareSourceCode
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """

    def __init__(self):
        self.schema = 'SoftwareSourceCode'


class codeRepositoryProp(SchemaProperty):

    """
    SchemaField for codeRepository
    Usage: Include in SchemaObject SchemaFields as your_django_field = codeRepositoryProp()  
    schema.org description:Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference URL"""

    _prop_schema = 'codeRepository'
    _expected_schema = 'URL'
    _enum = False
    _format_as = "ForeignKey"


class programmingLanguageProp(SchemaProperty):

    """
    SchemaField for programmingLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = programmingLanguageProp()  
    schema.org description:The computer programming language.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Language"""

    _prop_schema = 'programmingLanguage'
    _expected_schema = 'Language'
    _enum = False
    _format_as = "ForeignKey"


class codeSampleTypeProp(SchemaProperty):

    """
    SchemaField for codeSampleType
    Usage: Include in SchemaObject SchemaFields as your_django_field = codeSampleTypeProp()  
    schema.org description:Full (compile ready) solution, code snippet, inline code, scripts, template. Supersedes sampleType.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'codeSampleType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class runtimePlatformProp(SchemaProperty):

    """
    SchemaField for runtimePlatform
    Usage: Include in SchemaObject SchemaFields as your_django_field = runtimePlatformProp()  
    schema.org description:Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0). Supersedes runtime.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'runtimePlatform'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class targetProductProp(SchemaProperty):

    """
    SchemaField for targetProduct
    Usage: Include in SchemaObject SchemaFields as your_django_field = targetProductProp()  
    schema.org description:Target Operating System / Product to which the code applies. If applies to several versions, just the product name can be used.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SoftwareApplication"""

    _prop_schema = 'targetProduct'
    _expected_schema = 'SoftwareApplication'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
