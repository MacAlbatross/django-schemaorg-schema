# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ItemListSchema(SchemaObject):

    """Schema Mixin for ItemList
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A list of items of any sortfor example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.
    """

    def __init__(self):
        self.schema = 'ItemList'


class itemListElementProp(SchemaProperty):

    """
    SchemaField for itemListElement
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemListElementProp()  
    schema.org description:For itemListElement values, you can use simple strings (e.g. &quot;Peter&quot;, &quot;Paul&quot;, &quot;Mary&quot;), existing entities, or use ListItem. Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists. Note: The order of elements in your mark-up is not sufficient for indicating the order or elements. Use ListItem with a &#39;position&#39; property in such cases.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'itemListElement'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class numberOfItemsProp(SchemaProperty):

    """
    SchemaField for numberOfItems
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfItemsProp()  
    schema.org description:The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Integer"""

    _prop_schema = 'numberOfItems'
    _expected_schema = 'Integer'
    _enum = False
    _format_as = "ForeignKey"


class itemListOrderProp(SchemaProperty):

    """
    SchemaField for itemListOrder
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemListOrderProp()  
    schema.org description:Type of ordering (e.g. Ascending, Descending, Unordered).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'itemListOrder'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


# schema.org version 2.0
