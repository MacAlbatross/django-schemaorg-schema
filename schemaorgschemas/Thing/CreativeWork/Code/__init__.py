# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CodeSchema(SchemaObject):

    """Schema Mixin for Code
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Computer programming source code. Example: Full (compile ready) solutions, code snippet samples, scripts, templates.
    """

    def __init__(self):
        self.schema = 'Code'


class codeRepositoryProp(SchemaProperty):

    """
    SchemaField for codeRepository
    Usage: Include in SchemaObject SchemaFields as your_django_field = codeRepositoryProp()
    schema.org description:Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex)

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'codeRepository'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class programmingLanguageProp(SchemaProperty):

    """
    SchemaField for programmingLanguage
    Usage: Include in SchemaObject SchemaFields as your_django_field = programmingLanguageProp()
    schema.org description:The computer programming language.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'programmingLanguage'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class runtimeProp(SchemaProperty):

    """
    SchemaField for runtime
    Usage: Include in SchemaObject SchemaFields as your_django_field = runtimeProp()
    schema.org description:Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0)

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'runtime'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class sampleTypeProp(SchemaProperty):

    """
    SchemaField for sampleType
    Usage: Include in SchemaObject SchemaFields as your_django_field = sampleTypeProp()
    schema.org description:Full (compile ready) solution, code snippet, inline code, scripts, template.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'sampleType'
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
