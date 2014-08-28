# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NutritionInformationSchema(SchemaObject):

    """Schema Mixin for NutritionInformation
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Nutritional information about the recipe.
    """

    def __init__(self):
        self.schema = 'NutritionInformation'


class fatContentProp(SchemaProperty):

    """
    SchemaField for fatContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = fatContentProp()
    schema.org description:The number of grams of fat.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'fatContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class caloriesProp(SchemaProperty):

    """
    SchemaField for calories
    Usage: Include in SchemaObject SchemaFields as your_django_field = caloriesProp()
    schema.org description:The number of calories

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Energy"""

    _prop_schema = 'calories'
    _expected_schema = 'Energy'
    _enum = False
    _format_as = "ForeignKey"


class saturatedFatContentProp(SchemaProperty):

    """
    SchemaField for saturatedFatContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = saturatedFatContentProp()
    schema.org description:The number of grams of saturated fat.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'saturatedFatContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class unsaturatedFatContentProp(SchemaProperty):

    """
    SchemaField for unsaturatedFatContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = unsaturatedFatContentProp()
    schema.org description:The number of grams of unsaturated fat.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'unsaturatedFatContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class sodiumContentProp(SchemaProperty):

    """
    SchemaField for sodiumContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = sodiumContentProp()
    schema.org description:The number of milligrams of sodium.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'sodiumContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class fiberContentProp(SchemaProperty):

    """
    SchemaField for fiberContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = fiberContentProp()
    schema.org description:The number of grams of fiber.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'fiberContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class cholesterolContentProp(SchemaProperty):

    """
    SchemaField for cholesterolContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = cholesterolContentProp()
    schema.org description:The number of milligrams of cholesterol.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'cholesterolContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class carbohydrateContentProp(SchemaProperty):

    """
    SchemaField for carbohydrateContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = carbohydrateContentProp()
    schema.org description:The number of grams of carbohydrates.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'carbohydrateContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class sugarContentProp(SchemaProperty):

    """
    SchemaField for sugarContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = sugarContentProp()
    schema.org description:The number of grams of sugar.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'sugarContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class servingSizeProp(SchemaProperty):

    """
    SchemaField for servingSize
    Usage: Include in SchemaObject SchemaFields as your_django_field = servingSizeProp()
    schema.org description:The serving size, in terms of the number of volume or mass.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'servingSize'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class transFatContentProp(SchemaProperty):

    """
    SchemaField for transFatContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = transFatContentProp()
    schema.org description:The number of grams of trans fat.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'transFatContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"


class proteinContentProp(SchemaProperty):

    """
    SchemaField for proteinContent
    Usage: Include in SchemaObject SchemaFields as your_django_field = proteinContentProp()
    schema.org description:The number of grams of protein.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Mass"""

    _prop_schema = 'proteinContent'
    _expected_schema = 'Mass'
    _enum = False
    _format_as = "ForeignKey"
