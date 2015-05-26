# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Permit import validFromProp, validUntilProp, validInProp, validForProp, permitAudienceProp, issuedThroughProp, issuedByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GovernmentPermitSchema(SchemaObject):

    """Schema Mixin for GovernmentPermit
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A permit issued by a government agency.
    """

    def __init__(self):
        self.schema = 'GovernmentPermit'


# schema.org version 2.0
