# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.AnatomicalStructure import functionProp, associatedPathophysiologyProp, bodyLocationProp, relatedTherapyProp, connectedToProp, partOfSystemProp, diagramProp, relatedConditionProp, subStructureProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class NerveSchema(SchemaObject):

    """Schema Mixin for Nerve
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A common pathway for the electrochemical nerve impulses that are transmitted along each of the axons.
    """

    def __init__(self):
        self.schema = 'Nerve'


class sensoryUnitProp(SchemaProperty):

    """
    SchemaField for sensoryUnit
    Usage: Include in SchemaObject SchemaFields as your_django_field = sensoryUnitProp()  
    schema.org description:The neurological pathway extension that inputs and sends information to the brain or spinal cord.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'sensoryUnit'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class nerveMotorProp(SchemaProperty):

    """
    SchemaField for nerveMotor
    Usage: Include in SchemaObject SchemaFields as your_django_field = nerveMotorProp()  
    schema.org description:The neurological pathway extension that involves muscle control.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Muscle"""

    _prop_schema = 'nerveMotor'
    _expected_schema = 'Muscle'
    _enum = False
    _format_as = "ForeignKey"


class branchProp(SchemaProperty):

    """
    SchemaField for branch
    Usage: Include in SchemaObject SchemaFields as your_django_field = branchProp()  
    schema.org description:The branches that delineate from the nerve bundle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'branch'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class sourcedFromProp(SchemaProperty):

    """
    SchemaField for sourcedFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = sourcedFromProp()  
    schema.org description:The neurological pathway that originates the neurons.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference BrainStructure"""

    _prop_schema = 'sourcedFrom'
    _expected_schema = 'BrainStructure'
    _enum = False
    _format_as = "ForeignKey"
