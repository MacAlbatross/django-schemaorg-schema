# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalStudySchema(SchemaObject):

    """Schema Mixin for MedicalStudy
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A medical study is an umbrella type covering all kinds of research studies relating to human medicine or health, including observational studies and interventional trials and registries, randomized, controlled or not. When the specific type of study is known, use one of the extensions of this type, such as MedicalTrial or MedicalObservationalStudy. Also, note that this type should be used to mark up data that describes the study itself; to tag an article that publishes the results of a study, use MedicalScholarlyArticle. Note: use the code property of MedicalEntity to store study IDs, e.g. clinicaltrials.gov ID.
    """

    def __init__(self):
        self.schema = 'MedicalStudy'


class statusProp(SchemaProperty):

    """
    SchemaField for status
    Usage: Include in SchemaObject SchemaFields as your_django_field = statusProp()  
    schema.org description:The status of the study (enumerated).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalStudyStatus"""

    _prop_schema = 'status'
    _expected_schema = 'MedicalStudyStatus'
    _enum = False
    _format_as = "ForeignKey"


class studySubjectProp(SchemaProperty):

    """
    SchemaField for studySubject
    Usage: Include in SchemaObject SchemaFields as your_django_field = studySubjectProp()  
    schema.org description:A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalEntity"""

    _prop_schema = 'studySubject'
    _expected_schema = 'MedicalEntity'
    _enum = False
    _format_as = "ForeignKey"


class sponsorProp(SchemaProperty):

    """
    SchemaField for sponsor
    Usage: Include in SchemaObject SchemaFields as your_django_field = sponsorProp()  
    schema.org description:Sponsor of the study.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'sponsor'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class studyLocationProp(SchemaProperty):

    """
    SchemaField for studyLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = studyLocationProp()  
    schema.org description:The location in which the study is taking/took place.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AdministrativeArea"""

    _prop_schema = 'studyLocation'
    _expected_schema = 'AdministrativeArea'
    _enum = False
    _format_as = "ForeignKey"


class outcomeProp(SchemaProperty):

    """
    SchemaField for outcome
    Usage: Include in SchemaObject SchemaFields as your_django_field = outcomeProp()  
    schema.org description:Expected or actual outcomes of the study.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'outcome'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class populationProp(SchemaProperty):

    """
    SchemaField for population
    Usage: Include in SchemaObject SchemaFields as your_django_field = populationProp()  
    schema.org description:Any characteristics of the population used in the study, e.g. &#39;males under 65&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'population'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
