# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class InfectiousAgentClassSchema(SchemaObject):

    """Schema Mixin for InfectiousAgentClass
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Classes of agents or pathogens that transmit infectious diseases. Enumerated type.
    """

    def __init__(self):
        self.schema = 'InfectiousAgentClass'


/INFECTIOUSAGENTCLASS_CHOICES = (
    ('/FUNGUS', '/Fungus'),
    ('/MULTICELLULARPARASITE', '/MulticellularParasite'),
    ('/PRION', '/Prion'),
    ('/PROTOZOA', '/Protozoa'),
    ('/VIRUS', '/Virus'),
    ('/BACTERIA', '/Bacteria'),
)


class / infectiousAgentClassProp(SchemaEnumProperty):

    """
    Enumeration for /infectiousAgentClass
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/infectiousAgentClass'
    choices = /INFECTIOUSAGENTCLASS_CHOICES
    _format_as = "enum"
    adapter = {
        '/FUNGUS': '/Fungus',
        '/MULTICELLULARPARASITE': '/MulticellularParasite',
        '/PRION': '/Prion',
        '/PROTOZOA': '/Protozoa',
        '/VIRUS': '/Virus',
        '/BACTERIA': '/Bacteria',
    }


# schema.org version 2.0
