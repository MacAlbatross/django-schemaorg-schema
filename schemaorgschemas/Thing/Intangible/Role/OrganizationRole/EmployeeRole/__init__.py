# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Intangible.Role.OrganizationRole import numberedPositionProp
from schemaorgschemas.Thing.Intangible.Role import roleNameProp, endDateProp, startDateProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class EmployeeRoleSchema(SchemaObject):

    """Schema Mixin for EmployeeRole
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A subclass of OrganizationRole used to describe employee relationships.
    """

    def __init__(self):
        self.schema = 'EmployeeRole'


class baseSalaryProp(SchemaProperty):

    """
    SchemaField for baseSalary
    Usage: Include in SchemaObject SchemaFields as your_django_field = baseSalaryProp()  
    schema.org description:The base salary of the job or of an employee in an EmployeeRole.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'baseSalary'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class salaryCurrencyProp(SchemaProperty):

    """
    SchemaField for salaryCurrency
    Usage: Include in SchemaObject SchemaFields as your_django_field = salaryCurrencyProp()  
    schema.org description:The currency (coded using ISO 4217, http://en.wikipedia.org/wiki/ISO_4217 ) used for the main salary information in this job posting or for this employee.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'salaryCurrency'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
