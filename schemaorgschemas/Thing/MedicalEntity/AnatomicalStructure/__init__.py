# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class AnatomicalStructureSchema(SchemaObject):

    """Schema Mixin for AnatomicalStructure
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any part of the human body, typically a component of an anatomical system. Organs, tissues, and cells are all anatomical structures.
    """

    def __init__(self):
        self.schema = 'AnatomicalStructure'


class diagramProp(SchemaProperty):

    """
    SchemaField for diagram
    Usage: Include in SchemaObject SchemaFields as your_django_field = diagramProp()  
    schema.org description:An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'diagram'
    _expected_schema = 'ImageObject'
    _enum = False
    _format_as = "URLField"


class functionProp(SchemaProperty):

    """
    SchemaField for function
    Usage: Include in SchemaObject SchemaFields as your_django_field = functionProp()  
    schema.org description:Function of the anatomical structure.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'function'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class associatedPathophysiologyProp(SchemaProperty):

    """
    SchemaField for associatedPathophysiology
    Usage: Include in SchemaObject SchemaFields as your_django_field = associatedPathophysiologyProp()  
    schema.org description:If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'associatedPathophysiology'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class bodyLocationProp(SchemaProperty):

    """
    SchemaField for bodyLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = bodyLocationProp()  
    schema.org description:Location in the body of the anatomical structure.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'bodyLocation'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class relatedConditionProp(SchemaProperty):

    """
    SchemaField for relatedCondition
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedConditionProp()  
    schema.org description:A medical condition associated with this anatomy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalCondition"""

    _prop_schema = 'relatedCondition'
    _expected_schema = 'MedicalCondition'
    _enum = False
    _format_as = "ForeignKey"


class relatedTherapyProp(SchemaProperty):

    """
    SchemaField for relatedTherapy
    Usage: Include in SchemaObject SchemaFields as your_django_field = relatedTherapyProp()  
    schema.org description:A medical therapy related to this anatomy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTherapy"""

    _prop_schema = 'relatedTherapy'
    _expected_schema = 'MedicalTherapy'
    _enum = False
    _format_as = "ForeignKey"


class subStructureProp(SchemaProperty):

    """
    SchemaField for subStructure
    Usage: Include in SchemaObject SchemaFields as your_django_field = subStructureProp()  
    schema.org description:Component (sub-)structure(s) that comprise this anatomical structure.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'subStructure'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class connectedToProp(SchemaProperty):

    """
    SchemaField for connectedTo
    Usage: Include in SchemaObject SchemaFields as your_django_field = connectedToProp()  
    schema.org description:Other anatomical structures to which this structure is connected.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalStructure"""

    _prop_schema = 'connectedTo'
    _expected_schema = 'AnatomicalStructure'
    _enum = False
    _format_as = "ForeignKey"


class partOfSystemProp(SchemaProperty):

    """
    SchemaField for partOfSystem
    Usage: Include in SchemaObject SchemaFields as your_django_field = partOfSystemProp()  
    schema.org description:The anatomical or organ system that this structure is part of.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AnatomicalSystem"""

    _prop_schema = 'partOfSystem'
    _expected_schema = 'AnatomicalSystem'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
