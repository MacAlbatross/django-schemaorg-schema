# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy.LifestyleModification.PhysicalActivity import associatedAnatomyProp, categoryProp, pathophysiologyProp, epidemiologyProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy import contraindicationProp, indicationProp, adverseOutcomeProp, seriousAdverseOutcomeProp, duplicateTherapyProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ExercisePlanSchema(SchemaObject):

    """Schema Mixin for ExercisePlan
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Fitness-related activity designed for a specific health-related purpose, including defined exercise routines as well as activity prescribed by a clinician.
    """

    def __init__(self):
        self.schema = 'ExercisePlan'


class activityFrequencyProp(SchemaProperty):

    """
    SchemaField for activityFrequency
    Usage: Include in SchemaObject SchemaFields as your_django_field = activityFrequencyProp()  
    schema.org description:How often one should engage in the activity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'activityFrequency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class workloadProp(SchemaProperty):

    """
    SchemaField for workload
    Usage: Include in SchemaObject SchemaFields as your_django_field = workloadProp()  
    schema.org description:Quantitative measure of the physiologic output of the exercise; also referred to as energy expenditure.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Energy"""

    _prop_schema = 'workload'
    _expected_schema = 'Energy'
    _enum = False
    _format_as = "ForeignKey"


class activityDurationProp(SchemaProperty):

    """
    SchemaField for activityDuration
    Usage: Include in SchemaObject SchemaFields as your_django_field = activityDurationProp()  
    schema.org description:Length of time to engage in the activity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'activityDuration'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class exerciseTypeProp(SchemaProperty):

    """
    SchemaField for exerciseType
    Usage: Include in SchemaObject SchemaFields as your_django_field = exerciseTypeProp()  
    schema.org description:Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'exerciseType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class repetitionsProp(SchemaProperty):

    """
    SchemaField for repetitions
    Usage: Include in SchemaObject SchemaFields as your_django_field = repetitionsProp()  
    schema.org description:Number of times one should repeat the activity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'repetitions'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class restPeriodsProp(SchemaProperty):

    """
    SchemaField for restPeriods
    Usage: Include in SchemaObject SchemaFields as your_django_field = restPeriodsProp()  
    schema.org description:How often one should break from the activity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'restPeriods'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class intensityProp(SchemaProperty):

    """
    SchemaField for intensity
    Usage: Include in SchemaObject SchemaFields as your_django_field = intensityProp()  
    schema.org description:Quantitative measure gauging the degree of force involved in the exercise, for example, heartbeats per minute. May include the velocity of the movement.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'intensity'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class additionalVariableProp(SchemaProperty):

    """
    SchemaField for additionalVariable
    Usage: Include in SchemaObject SchemaFields as your_django_field = additionalVariableProp()  
    schema.org description:Any additional component of the exercise prescription that may need to be articulated to the patient. This may include the order of exercises, the number of repetitions of movement, quantitative distance, progressions over time, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'additionalVariable'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
