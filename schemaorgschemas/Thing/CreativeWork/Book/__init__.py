# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BookSchema(SchemaObject):

    """Schema Mixin for Book
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A book.
    """

    def __init__(self):
        self.schema = 'Book'


class bookEditionProp(SchemaProperty):

    """
    SchemaField for bookEdition
    Usage: Include in SchemaObject SchemaFields as your_django_field = bookEditionProp()
    schema.org description:The edition of the book.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'bookEdition'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class illustratorProp(SchemaProperty):

    """
    SchemaField for illustrator
    Usage: Include in SchemaObject SchemaFields as your_django_field = illustratorProp()
    schema.org description:The illustrator of the book.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'illustrator'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class bookFormatProp(SchemaProperty):

    """
    SchemaField for bookFormat
    Usage: Include in SchemaObject SchemaFields as your_django_field = bookFormatProp()
    schema.org description:The format of the book.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BookFormatType"""

    _prop_schema = 'bookFormat'
    _expected_schema = 'BookFormatType'
    _enum = False
    _format_as = "ForeignKey"


class isbnProp(SchemaProperty):

    """
    SchemaField for isbn
    Usage: Include in SchemaObject SchemaFields as your_django_field = isbnProp()
    schema.org description:The ISBN of the book.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'isbn'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class numberOfPagesProp(SchemaProperty):

    """
    SchemaField for numberOfPages
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfPagesProp()
    schema.org description:The number of pages in the book.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'numberOfPages'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"
