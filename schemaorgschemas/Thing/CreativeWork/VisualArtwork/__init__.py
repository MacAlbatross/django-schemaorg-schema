# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VisualArtworkSchema(SchemaObject):

    """Schema Mixin for VisualArtwork
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A work of art that is primarily visual in character.
    """

    def __init__(self):
        self.schema = 'VisualArtwork'


class artEditionProp(SchemaProperty):

    """
    SchemaField for artEdition
    Usage: Include in SchemaObject SchemaFields as your_django_field = artEditionProp()  
    schema.org description:The number of copies when multiple copies of a piece of artwork are produced - e.g. for a limited edition of 20 prints, &#39;artEdition&#39; refers to the total number of copies (in this example &quot;20&quot;).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'artEdition'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class depthProp(SchemaProperty):

    """
    SchemaField for depth
    Usage: Include in SchemaObject SchemaFields as your_django_field = depthProp()  
    schema.org description:The depth of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'depth'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class artworkSurfaceProp(SchemaProperty):

    """
    SchemaField for artworkSurface
    Usage: Include in SchemaObject SchemaFields as your_django_field = artworkSurfaceProp()  
    schema.org description:The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc. Supersedes surface.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'artworkSurface'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class artformProp(SchemaProperty):

    """
    SchemaField for artform
    Usage: Include in SchemaObject SchemaFields as your_django_field = artformProp()  
    schema.org description:e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'artform'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class artMediumProp(SchemaProperty):

    """
    SchemaField for artMedium
    Usage: Include in SchemaObject SchemaFields as your_django_field = artMediumProp()  
    schema.org description:The material used. (e.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.) Supersedes material.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'artMedium'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class widthProp(SchemaProperty):

    """
    SchemaField for width
    Usage: Include in SchemaObject SchemaFields as your_django_field = widthProp()  
    schema.org description:The width of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'width'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class heightProp(SchemaProperty):

    """
    SchemaField for height
    Usage: Include in SchemaObject SchemaFields as your_django_field = heightProp()  
    schema.org description:The height of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'height'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


# schema.org version 2.0
