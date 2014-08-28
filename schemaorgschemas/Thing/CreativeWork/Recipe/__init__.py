# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, creatorProp, textProp, citationProp, interactionCountProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, accessibilityFeatureProp, interactivityTypeProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, contentRatingProp, offersProp, editorProp, providerProp, publishingPrinciplesProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, copyrightHolderProp, genreProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, aggregateRatingProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, mentionsProp, audioProp, isBasedOnUrlProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class RecipeSchema(SchemaObject):

    """Schema Mixin for Recipe
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A recipe.
    """

    def __init__(self):
        self.schema = 'Recipe'


class totalTimeProp(SchemaProperty):

    """
    SchemaField for totalTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = totalTimeProp()
    schema.org description:The total time it takes to prepare and cook the recipe, in ISO 8601 duration format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'totalTime'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class nutritionProp(SchemaProperty):

    """
    SchemaField for nutrition
    Usage: Include in SchemaObject SchemaFields as your_django_field = nutritionProp()
    schema.org description:Nutrition information about the recipe.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference NutritionInformation"""

    _prop_schema = 'nutrition'
    _expected_schema = 'NutritionInformation'
    _enum = False
    _format_as = "ForeignKey"


class cookingMethodProp(SchemaProperty):

    """
    SchemaField for cookingMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = cookingMethodProp()
    schema.org description:The method of cooking, such as Frying, Steaming, ...

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'cookingMethod'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class recipeInstructionsProp(SchemaProperty):

    """
    SchemaField for recipeInstructions
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipeInstructionsProp()
    schema.org description:The steps to make the dish.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'recipeInstructions'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class recipeYieldProp(SchemaProperty):

    """
    SchemaField for recipeYield
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipeYieldProp()
    schema.org description:The quantity produced by the recipe (for example, number of people served, number of servings, etc).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'recipeYield'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class ingredientsProp(SchemaProperty):

    """
    SchemaField for ingredients
    Usage: Include in SchemaObject SchemaFields as your_django_field = ingredientsProp()
    schema.org description:An ingredient used in the recipe.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'ingredients'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class recipeCategoryProp(SchemaProperty):

    """
    SchemaField for recipeCategory
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipeCategoryProp()
    schema.org description:The category of the recipe-for example, appetizer, entree, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'recipeCategory'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class recipeCuisineProp(SchemaProperty):

    """
    SchemaField for recipeCuisine
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipeCuisineProp()
    schema.org description:The cuisine of the recipe (for example, French or Ethopian).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'recipeCuisine'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class prepTimeProp(SchemaProperty):

    """
    SchemaField for prepTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = prepTimeProp()
    schema.org description:The length of time it takes to prepare the recipe, in ISO 8601 duration format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'prepTime'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"


class cookTimeProp(SchemaProperty):

    """
    SchemaField for cookTime
    Usage: Include in SchemaObject SchemaFields as your_django_field = cookTimeProp()
    schema.org description:The time it takes to actually cook the dish, in ISO 8601 duration format.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Duration"""

    _prop_schema = 'cookTime'
    _expected_schema = 'Duration'
    _enum = False
    _format_as = "TimeField"
