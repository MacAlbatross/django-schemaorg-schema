# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalProcedureTypeSchema(SchemaObject):

    """Schema Mixin for MedicalProcedureType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An enumeration that describes different types of medical procedures.
    """

    def __init__(self):
        self.schema = 'MedicalProcedureType'


/PROCEDURETYPE_CHOICES = (
    ('/PERCUTANEOUSPROCEDURE', '/PercutaneousProcedure'),
    ('/SURGICALPROCEDURE', '/SurgicalProcedure'),
    ('/NONINVASIVEPROCEDURE', '/NoninvasiveProcedure'),
)


class / procedureTypeProp(SchemaEnumProperty):

    """
    Enumeration for /procedureType
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = '/procedureType'
    choices = /PROCEDURETYPE_CHOICES
    _format_as = "enum"
    adapter = {
        '/PERCUTANEOUSPROCEDURE': '/PercutaneousProcedure',
        '/SURGICALPROCEDURE': '/SurgicalProcedure',
        '/NONINVASIVEPROCEDURE': '/NoninvasiveProcedure',
    }


# schema.org version 2.0
