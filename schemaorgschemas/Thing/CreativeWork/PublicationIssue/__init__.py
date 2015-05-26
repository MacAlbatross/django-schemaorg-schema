# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PublicationIssueSchema(SchemaObject):

    """Schema Mixin for PublicationIssue
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A part of a successively published publication such as a periodical or publication volume, often numbered, usually containing a grouping of works such as articles.

      See also blog post.
    """

    def __init__(self):
        self.schema = 'PublicationIssue'


class paginationProp(SchemaProperty):

    """
    SchemaField for pagination
    Usage: Include in SchemaObject SchemaFields as your_django_field = paginationProp()  
    schema.org description:Any description of pages that is not separated into pageStart and pageEnd; for example, &quot;1-6, 9, 55&quot; or &quot;10-12, 46-49&quot;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'pagination'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class pageStartProp(SchemaProperty):

    """
    SchemaField for pageStart
    Usage: Include in SchemaObject SchemaFields as your_django_field = pageStartProp()  
    schema.org description:The page on which the work starts; for example &quot;135&quot; or &quot;xiii&quot;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'pageStart'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class issueNumberProp(SchemaProperty):

    """
    SchemaField for issueNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = issueNumberProp()  
    schema.org description:Identifies the issue of publication; for example, &quot;iii&quot; or &quot;2&quot;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'issueNumber'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class pageEndProp(SchemaProperty):

    """
    SchemaField for pageEnd
    Usage: Include in SchemaObject SchemaFields as your_django_field = pageEndProp()  
    schema.org description:The page on which the work ends; for example &quot;138&quot; or &quot;xvi&quot;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'pageEnd'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
