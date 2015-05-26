# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalProcedureSchema(SchemaObject):

    """Schema Mixin for MedicalProcedure
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A process of care used in either a diagnostic, therapeutic, or palliative capacity that relies on invasive (surgical), non-invasive, or percutaneous techniques.
    """

    def __init__(self):
        self.schema = 'MedicalProcedure'


class followupProp(SchemaProperty):

    """
    SchemaField for followup
    Usage: Include in SchemaObject SchemaFields as your_django_field = followupProp()  
    schema.org description:Typical or recommended followup care after the procedure is performed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'followup'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class preparationProp(SchemaProperty):

    """
    SchemaField for preparation
    Usage: Include in SchemaObject SchemaFields as your_django_field = preparationProp()  
    schema.org description:Typical preparation that a patient must undergo before having the procedure performed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'preparation'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class procedureTypeProp(SchemaProperty):

    """
    SchemaField for procedureType
    Usage: Include in SchemaObject SchemaFields as your_django_field = procedureTypeProp()  
    schema.org description:The type of procedure, for example Surgical, Noninvasive, or Percutaneous.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalProcedureType"""

    _prop_schema = 'procedureType'
    _expected_schema = 'MedicalProcedureType'
    _enum = False
    _format_as = "ForeignKey"


class howPerformedProp(SchemaProperty):

    """
    SchemaField for howPerformed
    Usage: Include in SchemaObject SchemaFields as your_django_field = howPerformedProp()  
    schema.org description:How the procedure is performed.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'howPerformed'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
