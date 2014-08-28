# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Product import isConsumableForProp, weightProp, isAccessoryOrSparePartForProp, colorProp, gtin8Prop, heightProp, releaseDateProp, isRelatedToProp, logoProp, productIDProp, skuProp, isSimilarToProp, reviewProp, audienceProp, widthProp, offersProp, mpnProp, brandProp, itemConditionProp, manufacturerProp, aggregateRatingProp, gtin14Prop, depthProp, gtin13Prop, modelProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class IndividualProductSchema(SchemaObject):

    """Schema Mixin for IndividualProduct
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A single, identifiable product instance (e.g. a laptop with a particular serial number).
    """

    def __init__(self):
        self.schema = 'IndividualProduct'


class serialNumberProp(SchemaProperty):

    """
    SchemaField for serialNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = serialNumberProp()
    schema.org description:The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'serialNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
