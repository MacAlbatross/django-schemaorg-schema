# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Service import serviceAreaProp, serviceTypeProp, availableChannelProp, reviewProp, providerProp, aggregateRatingProp, serviceOutputProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TaxiServiceSchema(SchemaObject):

    """Schema Mixin for TaxiService
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A service for a vehicle for hire with a driver for local travel. Fares are usually calculated based on distance traveled.
    """

    def __init__(self):
        self.schema = 'TaxiService'


# schema.org version 2.0
