# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.CreativeWork import commentProp, copyrightYearProp, versionProp, producerProp, creatorProp, publishingPrinciplesProp, textProp, citationProp, datePublishedProp, commentCountProp, associatedMediaProp, alternativeHeadlineProp, accountablePersonProp, videoProp, typicalAgeRangeProp, contributorProp, thumbnailUrlProp, mainEntityProp, accessibilityFeatureProp, interactivityTypeProp, publicationProp, discussionUrlProp, authorProp, headlineProp, reviewProp, encodingProp, characterProp, contentRatingProp, hasPartProp, exampleOfWorkProp, editorProp, providerProp, isPartOfProp, recordedAtProp, accessibilityHazardProp, dateModifiedProp, timeRequiredProp, educationalAlignmentProp, learningResourceTypeProp, awardProp, dateCreatedProp, translatorProp, offersProp, copyrightHolderProp, releasedEventProp, mentionsProp, genreProp, schemaVersionProp, contentLocationProp, educationalUseProp, accessibilityAPIProp, publisherProp, aboutProp, licenseProp, aggregateRatingProp, workExampleProp, sourceOrganizationProp, inLanguageProp, isFamilyFriendlyProp, audienceProp, accessibilityControlProp, keywordsProp, positionProp, audioProp, isBasedOnUrlProp

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
    schema.org description:A step or instruction involved in making the recipe.

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


class recipeIngredientProp(SchemaProperty):

    """
    SchemaField for recipeIngredient
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipeIngredientProp()  
    schema.org description:A single ingredient used in the recipe, e.g. sugar, flour or garlic. Supersedes ingredients.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'recipeIngredient'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class recipeCategoryProp(SchemaProperty):

    """
    SchemaField for recipeCategory
    Usage: Include in SchemaObject SchemaFields as your_django_field = recipeCategoryProp()  
    schema.org description:The category of the recipefor example, appetizer, entree, etc.

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
    schema.org description:The cuisine of the recipe (for example, French or Ethiopian).

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


# schema.org version 2.0
