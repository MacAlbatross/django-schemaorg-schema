# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp
from schemaorgschemas.Thing.MedicalEntity.AnatomicalStructure import functionProp, associatedPathophysiologyProp, bodyLocationProp, relatedTherapyProp, connectedToProp, partOfSystemProp, diagramProp, relatedConditionProp, subStructureProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MuscleSchema(SchemaObject):

    """Schema Mixin for Muscle
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A muscle is an anatomical structure consisting of a contractile form of tissue that animals use to effect movement.
    """

    def __init__(self):
        self.schema = 'Muscle'


class originProp(SchemaProperty):

    """
    SchemaField for origin
    Usage: Include in SchemaObject SchemaFields as your_django_field = originProp()
    schema.org description:The place or point where a muscle arises.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'origin'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class nerveProp(SchemaProperty):

    """
    SchemaField for nerve
    Usage: Include in SchemaObject SchemaFields as your_django_field = nerveProp()
    schema.org description:The underlying innervation associated with the muscle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Nerve"""

    _prop_schema = 'nerve'
    _expected_schema = 'Nerve'
    _enum = False
    _format_as = "ForeignKey"


class muscleActionProp(SchemaProperty):

    """
    SchemaField for muscleAction
    Usage: Include in SchemaObject SchemaFields as your_django_field = muscleActionProp()
    schema.org description:The movement the muscle generates. Supercedes action.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'muscleAction'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class insertionProp(SchemaProperty):

    """
    SchemaField for insertion
    Usage: Include in SchemaObject SchemaFields as your_django_field = insertionProp()
    schema.org description:The place of attachment of a muscle, or what the muscle moves.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'insertion'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class bloodSupplyProp(SchemaProperty):

    """
    SchemaField for bloodSupply
    Usage: Include in SchemaObject SchemaFields as your_django_field = bloodSupplyProp()
    schema.org description:The blood vessel that carries blood from the heart to the muscle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Vessel"""

    _prop_schema = 'bloodSupply'
    _expected_schema = 'Vessel'
    _enum = False
    _format_as = "ForeignKey"


class antagonistProp(SchemaProperty):

    """
    SchemaField for antagonist
    Usage: Include in SchemaObject SchemaFields as your_django_field = antagonistProp()
    schema.org description:The muscle whose action counteracts the specified muscle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Muscle"""

    _prop_schema = 'antagonist'
    _expected_schema = 'Muscle'
    _enum = False
    _format_as = "ForeignKey"
