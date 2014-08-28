# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalGuidelineSchema(SchemaObject):

    """Schema Mixin for MedicalGuideline
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement that denotes how to diagnose and treat a particular condition. Note: this type should be used to tag the actual guideline recommendation; if the guideline recommendation occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall article, not this type. Note also: the organization making the recommendation should be captured in the recognizingAuthority base property of MedicalEntity.
    """

    def __init__(self):
        self.schema = 'MedicalGuideline'


class evidenceLevelProp(SchemaProperty):

    """
    SchemaField for evidenceLevel
    Usage: Include in SchemaObject SchemaFields as your_django_field = evidenceLevelProp()
    schema.org description:Strength of evidence of the data used to formulate the guideline (enumerated).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalEvidenceLevel"""

    _prop_schema = 'evidenceLevel'
    _expected_schema = 'MedicalEvidenceLevel'
    _enum = False
    _format_as = "ForeignKey"


class evidenceOriginProp(SchemaProperty):

    """
    SchemaField for evidenceOrigin
    Usage: Include in SchemaObject SchemaFields as your_django_field = evidenceOriginProp()
    schema.org description:Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'evidenceOrigin'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class guidelineSubjectProp(SchemaProperty):

    """
    SchemaField for guidelineSubject
    Usage: Include in SchemaObject SchemaFields as your_django_field = guidelineSubjectProp()
    schema.org description:The medical conditions, treatments, etc. that are the subject of the guideline.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalEntity"""

    _prop_schema = 'guidelineSubject'
    _expected_schema = 'MedicalEntity'
    _enum = False
    _format_as = "ForeignKey"


class guidelineDateProp(SchemaProperty):

    """
    SchemaField for guidelineDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = guidelineDateProp()
    schema.org description:Date on which this guideline&#39;s recommendation was made.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'guidelineDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"
