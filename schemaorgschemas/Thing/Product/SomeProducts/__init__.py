# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Product import isConsumableForProp, weightProp, isAccessoryOrSparePartForProp, colorProp, purchaseDateProp, gtin8Prop, heightProp, releaseDateProp, aggregateRatingProp, logoProp, productIDProp, categoryProp, isSimilarToProp, reviewProp, audienceProp, widthProp, additionalPropertyProp, offersProp, productionDateProp, skuProp, mpnProp, brandProp, awardProp, itemConditionProp, manufacturerProp, isRelatedToProp, gtin14Prop, depthProp, gtin13Prop, gtin12Prop, modelProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class SomeProductsSchema(SchemaObject):

    """Schema Mixin for SomeProducts
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A placeholder for multiple similar products of the same kind.
    """

    def __init__(self):
        self.schema = 'SomeProducts'


class inventoryLevelProp(SchemaProperty):

    """
    SchemaField for inventoryLevel
    Usage: Include in SchemaObject SchemaFields as your_django_field = inventoryLevelProp()  
    schema.org description:The current approximate inventory level for the item or items.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'inventoryLevel'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


# schema.org version 2.0
