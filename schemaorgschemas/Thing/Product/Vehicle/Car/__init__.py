# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Product import isConsumableForProp, weightProp, isAccessoryOrSparePartForProp, colorProp, gtin8Prop, heightProp, releaseDateProp, isRelatedToProp, logoProp, productIDProp, skuProp, isSimilarToProp, reviewProp, audienceProp, widthProp, offersProp, mpnProp, brandProp, itemConditionProp, manufacturerProp, aggregateRatingProp, gtin14Prop, depthProp, gtin13Prop, modelProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CarSchema(SchemaObject):

    """Schema Mixin for Car
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An automobile.
    """

    def __init__(self):
        self.schema = 'Car'
