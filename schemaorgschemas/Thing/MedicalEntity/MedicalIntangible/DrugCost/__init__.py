# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.MedicalEntity import codeProp, relevantSpecialtyProp, studyProp, guidelineProp, recognizingAuthorityProp, medicineSystemProp, alternateNameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class DrugCostSchema(SchemaObject):

    """Schema Mixin for DrugCost
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The cost per unit of a medical drug. Note that this type is not meant to represent the price in an offer of a drug for sale; see the Offer type for that. This type will typically be used to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs of medical drugs vary widely depending on how and where they are paid for, so while this type captures some of the variables, costs should be used with caution by consumers of this schema&#39;s markup.
    """

    def __init__(self):
        self.schema = 'DrugCost'


class applicableLocationProp(SchemaProperty):

    """
    SchemaField for applicableLocation
    Usage: Include in SchemaObject SchemaFields as your_django_field = applicableLocationProp()
    schema.org description:The location in which the status applies.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AdministrativeArea"""

    _prop_schema = 'applicableLocation'
    _expected_schema = 'AdministrativeArea'
    _enum = False
    _format_as = "ForeignKey"


class drugUnitProp(SchemaProperty):

    """
    SchemaField for drugUnit
    Usage: Include in SchemaObject SchemaFields as your_django_field = drugUnitProp()
    schema.org description:The unit in which the drug is measured, e.g. &#39;5 mg tablet&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'drugUnit'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class costPerUnitProp(SchemaProperty):

    """
    SchemaField for costPerUnit
    Usage: Include in SchemaObject SchemaFields as your_django_field = costPerUnitProp()
    schema.org description:The cost per unit of the drug.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'costPerUnit'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class costCategoryProp(SchemaProperty):

    """
    SchemaField for costCategory
    Usage: Include in SchemaObject SchemaFields as your_django_field = costCategoryProp()
    schema.org description:The category of cost, such as wholesale, retail, reimbursement cap, etc.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference DrugCostCategory"""

    _prop_schema = 'costCategory'
    _expected_schema = 'DrugCostCategory'
    _enum = False
    _format_as = "ForeignKey"


class costCurrencyProp(SchemaProperty):

    """
    SchemaField for costCurrency
    Usage: Include in SchemaObject SchemaFields as your_django_field = costCurrencyProp()
    schema.org description:The currency (in 3-letter ISO 4217 format) of the drug cost.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'costCurrency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class costOriginProp(SchemaProperty):

    """
    SchemaField for costOrigin
    Usage: Include in SchemaObject SchemaFields as your_django_field = costOriginProp()
    schema.org description:Additional details to capture the origin of the cost data. For example, &#39;Medicare Part B&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'costOrigin'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"
