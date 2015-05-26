# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, resultProp, startTimeProp, errorProp, endTimeProp, locationProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Action.TransferAction import fromLocationProp, toLocationProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LendActionSchema(SchemaObject):

    """Schema Mixin for LendAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of providing an object under an agreement that it will be returned at a later date. Reciprocal of BorrowAction.Related actions:BorrowAction: Reciprocal of LendAction.
    """

    def __init__(self):
        self.schema = 'LendAction'


class borrowerProp(SchemaProperty):

    """
    SchemaField for borrower
    Usage: Include in SchemaObject SchemaFields as your_django_field = borrowerProp()  
    schema.org description:A sub property of participant. The person that borrows the object being lent.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Person"""

    _prop_schema = 'borrower'
    _expected_schema = 'Person'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
