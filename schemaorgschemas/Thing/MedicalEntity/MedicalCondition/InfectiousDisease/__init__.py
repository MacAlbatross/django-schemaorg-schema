# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.MedicalEntity.MedicalCondition import possibleComplicationProp, secondaryPreventionProp, naturalProgressionProp, epidemiologyProp, signOrSymptomProp, differentialDiagnosisProp, pathophysiologyProp, subtypeProp, possibleTreatmentProp, primaryPreventionProp, associatedAnatomyProp, expectedPrognosisProp, stageProp, causeProp, riskFactorProp, typicalTestProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class InfectiousDiseaseSchema(SchemaObject):

    """Schema Mixin for InfectiousDisease
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An infectious disease is a clinically evident human disease resulting from the presence of pathogenic microbial agents, like pathogenic viruses, pathogenic bacteria, fungi, protozoa, multicellular parasites, and prions. To be considered an infectious disease, such pathogens are known to be able to cause this disease.
    """

    def __init__(self):
        self.schema = 'InfectiousDisease'


class infectiousAgentProp(SchemaProperty):

    """
    SchemaField for infectiousAgent
    Usage: Include in SchemaObject SchemaFields as your_django_field = infectiousAgentProp()  
    schema.org description:The actual infectious agent, such as a specific bacterium.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'infectiousAgent'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class infectiousAgentClassProp(SchemaProperty):

    """
    SchemaField for infectiousAgentClass
    Usage: Include in SchemaObject SchemaFields as your_django_field = infectiousAgentClassProp()  
    schema.org description:The class of infectious agent (bacteria, prion, etc.) that causes the disease.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference InfectiousAgentClass"""

    _prop_schema = 'infectiousAgentClass'
    _expected_schema = 'InfectiousAgentClass'
    _enum = False
    _format_as = "ForeignKey"


class transmissionMethodProp(SchemaProperty):

    """
    SchemaField for transmissionMethod
    Usage: Include in SchemaObject SchemaFields as your_django_field = transmissionMethodProp()  
    schema.org description:How the disease spreads, either as a route or vector, for example &#39;direct contact&#39;, &#39;Aedes aegypti&#39;, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'transmissionMethod'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
