# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.AnatomicalStructure import functionProp, associatedPathophysiologyProp, bodyLocationProp, relatedTherapyProp, connectedToProp, partOfSystemProp, diagramProp, relatedConditionProp, subStructureProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LymphaticVesselSchema(SchemaObject):

    """Schema Mixin for LymphaticVessel
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A type of blood vessel that specifically carries lymph fluid unidirectionally toward the heart.
    """

    def __init__(self):
        self.schema = 'LymphaticVessel'


class regionDrainedProp(SchemaProperty):

    """
    SchemaField for regionDrained
    Usage: Include in SchemaObject SchemaFields as your_django_field = regionDrainedProp()
    schema.org description:The anatomical or organ system drained by this vessel; generally refers to a specific part of an organ.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'regionDrained'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class runsToProp(SchemaProperty):

    """
    SchemaField for runsTo
    Usage: Include in SchemaObject SchemaFields as your_django_field = runsToProp()
    schema.org description:The vasculature the lymphatic structure runs, or efferents, to.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Vessel"""

    _prop_schema = 'runsTo'
    _expected_schema = 'Vessel'
    _enum = False
    _format_as = "ForeignKey"


class originatesFromProp(SchemaProperty):

    """
    SchemaField for originatesFrom
    Usage: Include in SchemaObject SchemaFields as your_django_field = originatesFromProp()
    schema.org description:The vasculature the lymphatic structure originates, or afferents, from.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Vessel"""

    _prop_schema = 'originatesFrom'
    _expected_schema = 'Vessel'
    _enum = False
    _format_as = "ForeignKey"
