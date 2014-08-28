# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Product import isConsumableForProp, weightProp, isAccessoryOrSparePartForProp, colorProp, gtin8Prop, heightProp, releaseDateProp, isRelatedToProp, logoProp, productIDProp, skuProp, isSimilarToProp, reviewProp, audienceProp, widthProp, offersProp, mpnProp, brandProp, itemConditionProp, manufacturerProp, aggregateRatingProp, gtin14Prop, depthProp, gtin13Prop, modelProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ProductModelSchema(SchemaObject):

    """Schema Mixin for ProductModel
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A datasheet or vendor specification of a product (in the sense of a prototypical description).
    """

    def __init__(self):
        self.schema = 'ProductModel'


class predecessorOfProp(SchemaProperty):

    """
    SchemaField for predecessorOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = predecessorOfProp()  
    schema.org description:A pointer from a previous, often discontinued variant of the product to its newer variant.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ProductModel"""

    _prop_schema = 'predecessorOf'
    _expected_schema = 'ProductModel'
    _enum = False
    _format_as = "TextField"


class successorOfProp(SchemaProperty):

    """
    SchemaField for successorOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = successorOfProp()  
    schema.org description:A pointer from a newer variant of a product to its previous, often discontinued predecessor.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ProductModel"""

    _prop_schema = 'successorOf'
    _expected_schema = 'ProductModel'
    _enum = False
    _format_as = "TextField"


class isVariantOfProp(SchemaProperty):

    """
    SchemaField for isVariantOf
    Usage: Include in SchemaObject SchemaFields as your_django_field = isVariantOfProp()  
    schema.org description:A pointer to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ProductModel"""

    _prop_schema = 'isVariantOf'
    _expected_schema = 'ProductModel'
    _enum = False
    _format_as = "TextField"
