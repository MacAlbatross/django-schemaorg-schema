# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Organization import founderProp, foundingDateProp, telephoneProp, faxNumberProp, aggregateRatingProp, logoProp, eventProp, isicV4Prop, reviewProp, taxIDProp, memberProp, foundingLocationProp, locationProp, employeeProp, emailProp, seeksProp, numberOfEmployeesProp, subOrganizationProp, brandProp, ownsProp, awardProp, departmentProp, dissolutionDateProp, addressProp, dunsProp, contactPointProp, makesOfferProp, hasPOSProp, naicsProp, memberOfProp, legalNameProp, vatIDProp, globalLocationNumberProp
from schemaorgschemas.Thing.Organization.EducationalOrganization import alumniProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ElementarySchoolSchema(SchemaObject):

    """Schema Mixin for ElementarySchool
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An elementary school.
    """

    def __init__(self):
        self.schema = 'ElementarySchool'


# schema.org version 2.0
