# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing.Place.LocalBusiness import currenciesAcceptedProp, openingHoursProp, paymentAcceptedProp, priceRangeProp, parentOrganizationProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, hasMapProp, reviewProp, containedInProp, faxNumberProp, aggregateRatingProp, additionalPropertyProp, addressProp, telephoneProp, logoProp, geoProp, eventProp, globalLocationNumberProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class PhysicianSchema(SchemaObject):

    """Schema Mixin for Physician
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A doctor&#39;s office.
    """

    def __init__(self):
        self.schema = 'Physician'


class availableServiceProp(SchemaProperty):

    """
    SchemaField for availableService
    Usage: Include in SchemaObject SchemaFields as your_django_field = availableServiceProp()  
    schema.org description:A medical service available from this provider.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTherapy"""

    _prop_schema = 'availableService'
    _expected_schema = 'MedicalTherapy'
    _enum = False
    _format_as = "ForeignKey"


class hospitalAffiliationProp(SchemaProperty):

    """
    SchemaField for hospitalAffiliation
    Usage: Include in SchemaObject SchemaFields as your_django_field = hospitalAffiliationProp()  
    schema.org description:A hospital with which the physician or office is affiliated.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Hospital"""

    _prop_schema = 'hospitalAffiliation'
    _expected_schema = 'Hospital'
    _enum = False
    _format_as = "ForeignKey"


class medicalSpecialtyProp(SchemaProperty):

    """
    SchemaField for medicalSpecialty
    Usage: Include in SchemaObject SchemaFields as your_django_field = medicalSpecialtyProp()  
    schema.org description:A medical specialty of the provider.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalSpecialty"""

    _prop_schema = 'medicalSpecialty'
    _expected_schema = 'MedicalSpecialty'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
