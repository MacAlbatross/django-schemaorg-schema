# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.MedicalTherapy import contraindicationProp, indicationProp, adverseOutcomeProp, seriousAdverseOutcomeProp, duplicateTherapyProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DietSchema(SchemaObject):

    """Schema Mixin for Diet
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A strategy of regulating the intake of food to achieve or maintain a specific health-related goal.
    """

    def __init__(self):
        self.schema = 'Diet'


class proprietaryNameProp(SchemaProperty):

    """
    SchemaField for proprietaryName
    Usage: Include in SchemaObject SchemaFields as your_django_field = proprietaryNameProp()
    schema.org description:Proprietary name given to the diet plan, typically by its originator or creator.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'proprietaryName'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class risksProp(SchemaProperty):

    """
    SchemaField for risks
    Usage: Include in SchemaObject SchemaFields as your_django_field = risksProp()
    schema.org description:Specific physiologic risks associated to the plan.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'risks'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class physiologicalBenefitsProp(SchemaProperty):

    """
    SchemaField for physiologicalBenefits
    Usage: Include in SchemaObject SchemaFields as your_django_field = physiologicalBenefitsProp()
    schema.org description:Specific physiologic benefits associated to the plan.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'physiologicalBenefits'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class overviewProp(SchemaProperty):

    """
    SchemaField for overview
    Usage: Include in SchemaObject SchemaFields as your_django_field = overviewProp()
    schema.org description:Descriptive information establishing the overarching theory/philosophy of the plan. May include the rationale for the name, the population where the plan first came to prominence, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'overview'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class expertConsiderationsProp(SchemaProperty):

    """
    SchemaField for expertConsiderations
    Usage: Include in SchemaObject SchemaFields as your_django_field = expertConsiderationsProp()
    schema.org description:Medical expert advice related to the plan.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'expertConsiderations'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class endorsersProp(SchemaProperty):

    """
    SchemaField for endorsers
    Usage: Include in SchemaObject SchemaFields as your_django_field = endorsersProp()
    schema.org description:People or organizations that endorse the plan.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'endorsers'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class dietFeaturesProp(SchemaProperty):

    """
    SchemaField for dietFeatures
    Usage: Include in SchemaObject SchemaFields as your_django_field = dietFeaturesProp()
    schema.org description:Nutritional information specific to the dietary plan. May include dietary recommendations on what foods to avoid, what foods to consume, and specific alterations/deviations from the USDA or other regulatory body&#39;s approved dietary guidelines.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dietFeatures'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
