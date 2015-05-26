# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, positionProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MusicCompositionSchema(SchemaObject):

    """Schema Mixin for MusicComposition
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A musical composition.
    """

    def __init__(self):
        self.schema = 'MusicComposition'


class musicCompositionFormProp(SchemaProperty):

    """
    SchemaField for musicCompositionForm
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicCompositionFormProp()  
    schema.org description:The type of composition (e.g. overture, sonata, symphony, etc.).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'musicCompositionForm'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class musicArrangementProp(SchemaProperty):

    """
    SchemaField for musicArrangement
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicArrangementProp()  
    schema.org description:An arrangement derived from the composition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicComposition"""

    _prop_schema = 'musicArrangement'
    _expected_schema = 'MusicComposition'
    _enum = False
    _format_as = "ForeignKey"


class includedCompositionProp(SchemaProperty):

    """
    SchemaField for includedComposition
    Usage: Include in SchemaObject SchemaFields as your_django_field = includedCompositionProp()  
    schema.org description:Smaller compositions included in this work (e.g. a movement in a symphony).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicComposition"""

    _prop_schema = 'includedComposition'
    _expected_schema = 'MusicComposition'
    _enum = False
    _format_as = "ForeignKey"


class composerProp(SchemaProperty):

    """
    SchemaField for composer
    Usage: Include in SchemaObject SchemaFields as your_django_field = composerProp()  
    schema.org description:The person or organization who wrote the composition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'composer'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class firstPerformanceProp(SchemaProperty):

    """
    SchemaField for firstPerformance
    Usage: Include in SchemaObject SchemaFields as your_django_field = firstPerformanceProp()  
    schema.org description:The date and place the work was first performed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Event"""

    _prop_schema = 'firstPerformance'
    _expected_schema = 'Event'
    _enum = False
    _format_as = "ForeignKey"


class lyricistProp(SchemaProperty):

    """
    SchemaField for lyricist
    Usage: Include in SchemaObject SchemaFields as your_django_field = lyricistProp()  
    schema.org description:The person who wrote the words.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'lyricist'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


class musicalKeyProp(SchemaProperty):

    """
    SchemaField for musicalKey
    Usage: Include in SchemaObject SchemaFields as your_django_field = musicalKeyProp()  
    schema.org description:The key, mode, or scale this composition uses.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'musicalKey'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class recordedAsProp(SchemaProperty):

    """
    SchemaField for recordedAs
    Usage: Include in SchemaObject SchemaFields as your_django_field = recordedAsProp()  
    schema.org description:An audio recording of the work. Inverse property: recordingOf.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MusicRecording"""

    _prop_schema = 'recordedAs'
    _expected_schema = 'MusicRecording'
    _enum = False
    _format_as = "ForeignKey"


class iswcCodeProp(SchemaProperty):

    """
    SchemaField for iswcCode
    Usage: Include in SchemaObject SchemaFields as your_django_field = iswcCodeProp()  
    schema.org description:The International Standard Musical Work Code for the composition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'iswcCode'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
