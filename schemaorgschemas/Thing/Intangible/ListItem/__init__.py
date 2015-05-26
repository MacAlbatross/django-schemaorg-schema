# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ListItemSchema(SchemaObject):

    """Schema Mixin for ListItem
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    An list item, e.g. a step in a checklist or how-to description.
    """

    def __init__(self):
        self.schema = 'ListItem'


class itemProp(SchemaProperty):

    """
    SchemaField for item
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemProp()  
    schema.org description:An entity represented by an entry in a list (e.g. an &#39;artist&#39; in a list of &#39;artists&#39;)&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Thing"""

    _prop_schema = 'item'
    _expected_schema = 'Thing'
    _enum = False
    _format_as = "TextField"


class previousItemProp(SchemaProperty):

    """
    SchemaField for previousItem
    Usage: Include in SchemaObject SchemaFields as your_django_field = previousItemProp()  
    schema.org description:A link to the ListItem that preceeds the current one.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ListItem"""

    _prop_schema = 'previousItem'
    _expected_schema = 'ListItem'
    _enum = False
    _format_as = "ForeignKey"


class nextItemProp(SchemaProperty):

    """
    SchemaField for nextItem
    Usage: Include in SchemaObject SchemaFields as your_django_field = nextItemProp()  
    schema.org description:A link to the ListItem that follows the current one.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ListItem"""

    _prop_schema = 'nextItem'
    _expected_schema = 'ListItem'
    _enum = False
    _format_as = "ForeignKey"


class positionProp(SchemaProperty):

    """
    SchemaField for position
    Usage: Include in SchemaObject SchemaFields as your_django_field = positionProp()  
    schema.org description:The position of an item in a series or sequence of items.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'position'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
