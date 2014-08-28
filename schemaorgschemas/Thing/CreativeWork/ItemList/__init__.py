# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ItemListSchema(SchemaObject):

    """Schema Mixin for ItemList
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A list of items of any sort-for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.
    """

    def __init__(self):
        self.schema = 'ItemList'


class itemListElementProp(SchemaProperty):

    """
    SchemaField for itemListElement
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemListElementProp()  
    schema.org description:A single list item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'itemListElement'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class itemListOrderProp(SchemaProperty):

    """
    SchemaField for itemListOrder
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemListOrderProp()  
    schema.org description:Type of ordering (e.g. Ascending, Descending, Unordered).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'itemListOrder'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
