# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.Intangible.ItemList import itemListElementProp, numberOfItemsProp, itemListOrderProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class BreadcrumbListSchema(SchemaObject):

    """Schema Mixin for BreadcrumbList
    Usage: place after django model in class definition, schema will return the schema.org url for the object

      A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page.


      The &#39;position&#39; property is used to reconstruct the order of the items in a BreadcrumbList.
      The convention is that a breadcrumb list has an itemListOrder of ItemListOrderAscending (lower values listed first), and that the
      first items in this list correspond to the &quot;top&quot; or beginning of the breadcrumb trail, e.g. with a site or section homepage.
      The specific values of &#39;position&#39; are not assigned meaning for a BreadcrumbList, but they should be integers, e.g. beginning
      with &#39;1&#39; for the first item in the list.

    """

    def __init__(self):
        self.schema = 'BreadcrumbList'


# schema.org version 2.0
