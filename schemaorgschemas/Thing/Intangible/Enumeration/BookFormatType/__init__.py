# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BookFormatTypeSchema(SchemaObject):

    """Schema Mixin for BookFormatType
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The publication format of the book.
    """

    def __init__(self):
        self.schema = 'BookFormatType'


BOOKFORMAT_CHOICES = (
    ('HARDCOVER', 'Hardcover: Book format: Hardcover.'),
    ('PAPERBACK', 'Paperback: Book format: Paperback.'),
    ('EBOOK', 'EBook: Book format: Ebook.'),
)


class bookFormatProp(SchemaEnumProperty):

    """
    Enumeration for bookFormat
    Prepoulated with the Schema.org choices
    """
    _enum = True
    _prop_schema = 'bookFormat'
    choices = BOOKFORMAT_CHOICES
    _format_as = "enum"
    adapter = {
        'HARDCOVER': 'Hardcover',
        'PAPERBACK': 'Paperback',
        'EBOOK': 'EBook',
    }
