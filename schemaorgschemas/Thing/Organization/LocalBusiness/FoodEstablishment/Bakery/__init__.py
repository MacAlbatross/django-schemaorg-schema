# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Place import isicV4Prop, mapProp, openingHoursSpecificationProp, photoProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, telephoneProp, addressProp, interactionCountProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, branchOfProp, priceRangeProp
from schemaorgschemas.Thing.Organization.LocalBusiness.FoodEstablishment import menuProp, servesCuisineProp, acceptsReservationsProp
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, interactionCountProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, locationProp, employeeProp, emailProp, seeksProp, subOrganizationProp, brandProp, ownsProp, telephoneProp, departmentProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BakerySchema(SchemaObject):

    """Schema Mixin for Bakery
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A bakery.
    """

    def __init__(self):
        self.schema = 'Bakery'
