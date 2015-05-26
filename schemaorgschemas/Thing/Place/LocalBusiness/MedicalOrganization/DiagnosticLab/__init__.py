# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, priceRangeProp, parentOrganizationProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DiagnosticLabSchema(SchemaObject):

    """Schema Mixin for DiagnosticLab
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A medical laboratory that offers on-site or off-site diagnostic services.
    """

    def __init__(self):
        self.schema = 'DiagnosticLab'


class availableTestProp(SchemaProperty):

    """
    SchemaField for availableTest
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableTestProp()  
    schema.org description:A diagnostic test or procedure offered by this lab.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTest"""

    _prop_schema = 'availableTest'
    _expected_schema = 'MedicalTest'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
