# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class MedicalDeviceSchema(SchemaObject):

    """Schema Mixin for MedicalDevice
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any object used in a medical capacity, such as to diagnose or treat a patient.
    """

    def __init__(self):
        self.schema = 'MedicalDevice'


class contraindicationProp(SchemaProperty):

    """
    SchemaField for contraindication
    Usage: Include in SchemaObject SchemaFields as your_django_field = contraindicationProp()  
    schema.org description:A contraindication for this therapy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalContraindication"""

    _prop_schema = 'contraindication'
    _expected_schema = 'MedicalContraindication'
    _enum = False
    _format_as = "ForeignKey"


class indicationProp(SchemaProperty):

    """
    SchemaField for indication
    Usage: Include in SchemaObject SchemaFields as your_django_field = indicationProp()  
    schema.org description:A factor that indicates use of this therapy for treatment and/or prevention of a condition, symptom, etc. For therapies such as drugs, indications can include both officially-approved indications as well as off-label uses. These can be distinguished by using the ApprovedIndication subtype of MedicalIndication.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalIndication"""

    _prop_schema = 'indication'
    _expected_schema = 'MedicalIndication'
    _enum = False
    _format_as = "ForeignKey"


class purposeProp(SchemaProperty):

    """
    SchemaField for purpose
    Usage: Include in SchemaObject SchemaFields as your_django_field = purposeProp()  
    schema.org description:A goal towards an action is taken. Can be concrete or abstract.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'purpose'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class preOpProp(SchemaProperty):

    """
    SchemaField for preOp
    Usage: Include in SchemaObject SchemaFields as your_django_field = preOpProp()  
    schema.org description:A description of the workup, testing, and other preparations required before implanting this device.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'preOp'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class postOpProp(SchemaProperty):

    """
    SchemaField for postOp
    Usage: Include in SchemaObject SchemaFields as your_django_field = postOpProp()  
    schema.org description:A description of the postoperative procedures, care, and/or followups for this device.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'postOp'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class adverseOutcomeProp(SchemaProperty):

    """
    SchemaField for adverseOutcome
    Usage: Include in SchemaObject SchemaFields as your_django_field = adverseOutcomeProp()  
    schema.org description:A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or is otherwise life-threatening or requires immediate medical attention), tag it as a seriouseAdverseOutcome instead.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalEntity"""

    _prop_schema = 'adverseOutcome'
    _expected_schema = 'MedicalEntity'
    _enum = False
    _format_as = "ForeignKey"


class seriousAdverseOutcomeProp(SchemaProperty):

    """
    SchemaField for seriousAdverseOutcome
    Usage: Include in SchemaObject SchemaFields as your_django_field = seriousAdverseOutcomeProp()  
    schema.org description:A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference MedicalEntity"""

    _prop_schema = 'seriousAdverseOutcome'
    _expected_schema = 'MedicalEntity'
    _enum = False
    _format_as = "ForeignKey"


class procedureProp(SchemaProperty):

    """
    SchemaField for procedure
    Usage: Include in SchemaObject SchemaFields as your_django_field = procedureProp()  
    schema.org description:A description of the procedure involved in setting up, using, and/or installing the device.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'procedure'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
