# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CreativeWorkSeriesSchema(SchemaObject):

    """Schema Mixin for CreativeWorkSeries
    Usage: place after django model in class definition, schema will return the schema.org url for the object

          A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind.
          CreativeWorkSeries are usually organized into some order, often chronological. Unlike ItemList which
          is a general purpose data structure for lists of things, the emphasis with
          CreativeWorkSeries is on published materials (written e.g. books and periodicals,
          or media such as tv, radio and games).



          Specific subtypes are available for describing TVSeries, RadioSeries,
          MovieSeries,
          BookSeries,
          Periodical
          and VideoGameSeries. In each case,
          the hasPart / isPartOf properties
          can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
          just to organize these more specific and practical subtypes.



          It is common for properties applicable to an item from the series to be usefully applied to the containing group.
          Schema.org attempts to anticipate some of these cases, but publishers should be free to apply
          properties of the series parts to the series as a whole wherever they seem appropriate.
    """

    def __init__(self):
        self.schema = 'CreativeWorkSeries'


class startDateProp(SchemaProperty):

    """
    SchemaField for startDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = startDateProp()  
    schema.org description:The start date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'startDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class endDateProp(SchemaProperty):

    """
    SchemaField for endDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = endDateProp()  
    schema.org description:The end date and time of the item (in ISO 8601 date format).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'endDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


# schema.org version 2.0
