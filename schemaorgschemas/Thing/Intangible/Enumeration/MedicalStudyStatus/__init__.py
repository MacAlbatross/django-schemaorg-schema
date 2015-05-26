# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp
from schemaorgschemas.Thing.Intangible.Enumeration import supersededByProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalStudyStatusSchema(SchemaObject):

    """Schema Mixin for MedicalStudyStatus
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The status of a medical study. Enumerated type.
    """

    def __init__(self):
        self.schema = 'MedicalStudyStatus'


STATUS_CHOICES = (
    ('COMPLETED', 'Completed: Completed.'),
    ('ENROLLINGBYINVITATION',
     'EnrollingByInvitation: Enrolling participants by invitation only.'),
    ('NOTYETRECRUITING', 'NotYetRecruiting: Not yet recruiting.'),
    ('RECRUITING', 'Recruiting: Recruiting participants.'),
    ('RESULTSAVAILABLE', 'ResultsAvailable: Results are available.'),
    ('RESULTSNOTAVAILABLE', 'ResultsNotAvailable: Results are not available.'),
    ('SUSPENDED', 'Suspended: Suspended.'),
    ('TERMINATED', 'Terminated: Terminated.'),
    ('WITHDRAWN', 'Withdrawn: Withdrawn.'),
    ('ACTIVENOTRECRUITING',
     'ActiveNotRecruiting: Active, but not recruiting new participants.'),
)


class statusProp(SchemaEnumProperty):

    """
    Enumeration for status
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'status'
    choices = STATUS_CHOICES
    _format_as = "enum"
    adapter = {
        'COMPLETED': 'Completed',
        'ENROLLINGBYINVITATION': 'EnrollingByInvitation',
        'NOTYETRECRUITING': 'NotYetRecruiting',
        'RECRUITING': 'Recruiting',
        'RESULTSAVAILABLE': 'ResultsAvailable',
        'RESULTSNOTAVAILABLE': 'ResultsNotAvailable',
        'SUSPENDED': 'Suspended',
        'TERMINATED': 'Terminated',
        'WITHDRAWN': 'Withdrawn',
        'ACTIVENOTRECRUITING': 'ActiveNotRecruiting',
    }


# schema.org version 2.0
