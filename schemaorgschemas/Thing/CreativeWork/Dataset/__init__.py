# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DatasetSchema(SchemaObject):

    """Schema Mixin for Dataset
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A body of structured information describing some topic(s) of interest.
    """

    def __init__(self):
        self.schema = 'Dataset'


class catalogProp(SchemaProperty):

    """
    SchemaField for catalog
    Usage: Include in SchemaObject SchemaFields as your_django_field = catalogProp()  
    schema.org description:A data catalog which contains a dataset.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DataCatalog"""

    _prop_schema = 'catalog'
    _expected_schema = 'DataCatalog'
    _enum = False
    _format_as = "ForeignKey"


class temporalProp(SchemaProperty):

    """
    SchemaField for temporal
    Usage: Include in SchemaObject SchemaFields as your_django_field = temporalProp()  
    schema.org description:The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'temporal'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


class distributionProp(SchemaProperty):

    """
    SchemaField for distribution
    Usage: Include in SchemaObject SchemaFields as your_django_field = distributionProp()  
    schema.org description:A downloadable form of this dataset, at a specific location, in a specific format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DataDownload"""

    _prop_schema = 'distribution'
    _expected_schema = 'DataDownload'
    _enum = False
    _format_as = "ForeignKey"


class spatialProp(SchemaProperty):

    """
    SchemaField for spatial
    Usage: Include in SchemaObject SchemaFields as your_django_field = spatialProp()  
    schema.org description:The range of spatial applicability of a dataset, e.g. for a dataset of New York weather, the state of New York.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Place"""

    _prop_schema = 'spatial'
    _expected_schema = 'Place'
    _enum = False
    _format_as = "TextField"
