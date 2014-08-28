# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalConditionSchema(SchemaObject):

    """Schema Mixin for MedicalCondition
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any condition of the human body that affects the normal functioning of a person, whether physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes, etc.
    """

    def __init__(self):
        self.schema = 'MedicalCondition'


class possibleComplicationProp(SchemaProperty):

    """
    SchemaField for possibleComplication
    Usage: Include in SchemaObject SchemaFields as your_django_field = possibleComplicationProp()  
    schema.org description:A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'possibleComplication'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class secondaryPreventionProp(SchemaProperty):

    """
    SchemaField for secondaryPrevention
    Usage: Include in SchemaObject SchemaFields as your_django_field = secondaryPreventionProp()  
    schema.org description:A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTherapy"""

    _prop_schema = 'secondaryPrevention'
    _expected_schema = 'MedicalTherapy'
    _enum = False
    _format_as = "ForeignKey"


class naturalProgressionProp(SchemaProperty):

    """
    SchemaField for naturalProgression
    Usage: Include in SchemaObject SchemaFields as your_django_field = naturalProgressionProp()  
    schema.org description:The expected progression of the condition if it is not treated and allowed to progress naturally.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'naturalProgression'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class subtypeProp(SchemaProperty):

    """
    SchemaField for subtype
    Usage: Include in SchemaObject SchemaFields as your_django_field = subtypeProp()  
    schema.org description:A more specific type of the condition, where applicable, for example &#39;Type 1 Diabetes&#39;, &#39;Type 2 Diabetes&#39;, or &#39;Gestational Diabetes&#39; for Diabetes.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'subtype'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class signOrSymptomProp(SchemaProperty):

    """
    SchemaField for signOrSymptom
    Usage: Include in SchemaObject SchemaFields as your_django_field = signOrSymptomProp()  
    schema.org description:A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experience of the medical condition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalSignOrSymptom"""

    _prop_schema = 'signOrSymptom'
    _expected_schema = 'MedicalSignOrSymptom'
    _enum = False
    _format_as = "ForeignKey"


class differentialDiagnosisProp(SchemaProperty):

    """
    SchemaField for differentialDiagnosis
    Usage: Include in SchemaObject SchemaFields as your_django_field = differentialDiagnosisProp()  
    schema.org description:One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DDxElement"""

    _prop_schema = 'differentialDiagnosis'
    _expected_schema = 'DDxElement'
    _enum = False
    _format_as = "ForeignKey"


class pathophysiologyProp(SchemaProperty):

    """
    SchemaField for pathophysiology
    Usage: Include in SchemaObject SchemaFields as your_django_field = pathophysiologyProp()  
    schema.org description:Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'pathophysiology'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class epidemiologyProp(SchemaProperty):

    """
    SchemaField for epidemiology
    Usage: Include in SchemaObject SchemaFields as your_django_field = epidemiologyProp()  
    schema.org description:The characteristics of associated patients, such as age, gender, race etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'epidemiology'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class possibleTreatmentProp(SchemaProperty):

    """
    SchemaField for possibleTreatment
    Usage: Include in SchemaObject SchemaFields as your_django_field = possibleTreatmentProp()  
    schema.org description:A possible treatment to address this condition, sign or symptom.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTherapy"""

    _prop_schema = 'possibleTreatment'
    _expected_schema = 'MedicalTherapy'
    _enum = False
    _format_as = "ForeignKey"


class primaryPreventionProp(SchemaProperty):

    """
    SchemaField for primaryPrevention
    Usage: Include in SchemaObject SchemaFields as your_django_field = primaryPreventionProp()  
    schema.org description:A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTherapy"""

    _prop_schema = 'primaryPrevention'
    _expected_schema = 'MedicalTherapy'
    _enum = False
    _format_as = "ForeignKey"


class associatedAnatomyProp(SchemaProperty):

    """
    SchemaField for associatedAnatomy
    Usage: Include in SchemaObject SchemaFields as your_django_field = associatedAnatomyProp()  
    schema.org description:The anatomy of the underlying organ system or structures associated with this entity.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SuperficialAnatomy"""

    _prop_schema = 'associatedAnatomy'
    _expected_schema = 'SuperficialAnatomy'
    _enum = False
    _format_as = "ForeignKey"


class expectedPrognosisProp(SchemaProperty):

    """
    SchemaField for expectedPrognosis
    Usage: Include in SchemaObject SchemaFields as your_django_field = expectedPrognosisProp()  
    schema.org description:The likely outcome in either the short term or long term of the medical condition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'expectedPrognosis'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class typicalTestProp(SchemaProperty):

    """
    SchemaField for typicalTest
    Usage: Include in SchemaObject SchemaFields as your_django_field = typicalTestProp()  
    schema.org description:A medical test typically performed given this condition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalTest"""

    _prop_schema = 'typicalTest'
    _expected_schema = 'MedicalTest'
    _enum = False
    _format_as = "ForeignKey"


class causeProp(SchemaProperty):

    """
    SchemaField for cause
    Usage: Include in SchemaObject SchemaFields as your_django_field = causeProp()  
    schema.org description:An underlying cause. More specifically, one of the causative agent(s) that are most directly responsible for the pathophysiologic process that eventually results in the occurrence.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalCause"""

    _prop_schema = 'cause'
    _expected_schema = 'MedicalCause'
    _enum = False
    _format_as = "ForeignKey"


class riskFactorProp(SchemaProperty):

    """
    SchemaField for riskFactor
    Usage: Include in SchemaObject SchemaFields as your_django_field = riskFactorProp()  
    schema.org description:A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age, coexisting condition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalRiskFactor"""

    _prop_schema = 'riskFactor'
    _expected_schema = 'MedicalRiskFactor'
    _enum = False
    _format_as = "ForeignKey"


class stageProp(SchemaProperty):

    """
    SchemaField for stage
    Usage: Include in SchemaObject SchemaFields as your_django_field = stageProp()  
    schema.org description:The stage of the condition, if applicable.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalConditionStage"""

    _prop_schema = 'stage'
    _expected_schema = 'MedicalConditionStage'
    _enum = False
    _format_as = "ForeignKey"
