# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DatasetSchema(SchemaObject):

    """Schema Mixin for Dataset
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A body of structured information describing some topic(s) of interest.
    """

    def __init__(self):
        self.schema = 'Dataset'


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


class includedDataCatalogProp(SchemaProperty):

    """
    SchemaField for includedDataCatalog
    Usage: Include in SchemaObject SchemaFields as your_django_field = includedDataCatalogProp()  
    schema.org description:A data catalog contained in the dataset. Supersedes catalog.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DataCatalog"""

    _prop_schema = 'includedDataCatalog'
    _expected_schema = 'DataCatalog'
    _enum = False
    _format_as = "ForeignKey"


class datasetTimeIntervalProp(SchemaProperty):

    """
    SchemaField for datasetTimeInterval
    Usage: Include in SchemaObject SchemaFields as your_django_field = datasetTimeIntervalProp()  
    schema.org description:The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format). Supersedes temporal.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'datasetTimeInterval'
    _expected_schema = None
    _enum = False
    _format_as = "DateTimeField"


# schema.org version 2.0
