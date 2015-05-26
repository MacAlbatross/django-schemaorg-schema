# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DDxElementSchema(SchemaObject):

    """Schema Mixin for DDxElement
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An alternative, closely-related condition typically considered later in the differential diagnosis process along with the signs that are used to distinguish it.
    """

    def __init__(self):
        self.schema = 'DDxElement'


class distinguishingSignProp(SchemaProperty):

    """
    SchemaField for distinguishingSign
    Usage: Include in SchemaObject SchemaFields as your_django_field = distinguishingSignProp()  
    schema.org description:One of a set of signs and symptoms that can be used to distinguish this diagnosis from others in the differential diagnosis.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalSignOrSymptom"""

    _prop_schema = 'distinguishingSign'
    _expected_schema = 'MedicalSignOrSymptom'
    _enum = False
    _format_as = "ForeignKey"


class diagnosisProp(SchemaProperty):

    """
    SchemaField for diagnosis
    Usage: Include in SchemaObject SchemaFields as your_django_field = diagnosisProp()  
    schema.org description:One or more alternative conditions considered in the differential diagnosis process.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalCondition"""

    _prop_schema = 'diagnosis'
    _expected_schema = 'MedicalCondition'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
