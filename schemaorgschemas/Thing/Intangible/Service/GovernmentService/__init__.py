# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Intangible.Service import serviceAreaProp, serviceTypeProp, serviceAudienceProp, availableChannelProp, producesProp, providerProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class GovernmentServiceSchema(SchemaObject):

    """Schema Mixin for GovernmentService
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A service provided by a government organization, e.g. food stamps, veterans benefits, etc.
    """

    def __init__(self):
        self.schema = 'GovernmentService'


class serviceOperatorProp(SchemaProperty):

    """
    SchemaField for serviceOperator
    Usage: Include in SchemaObject SchemaFields as your_django_field = serviceOperatorProp()
    schema.org description:The operating organization, if different from the provider. This enables the representation of services that are provided by an organization, but operated by another organization like a subcontractor.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'serviceOperator'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"
