# -*- coding: utf-8 -*-
from schemaorgschemas.Thing.Action import participantProp, targetProp, objectProp, agentProp, actionStatusProp, instrumentProp, locationProp, startTimeProp, errorProp, endTimeProp, resultProp
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class TradeActionSchema(SchemaObject):

    """Schema Mixin for TradeAction
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.
    """

    def __init__(self):
        self.schema = 'TradeAction'


class priceProp(SchemaProperty):

    """
    SchemaField for price
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceProp()  
    schema.org description:The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.  Usage guidelines:  Use the priceCurrency property (with ISO 4217 codes e.g. &quot;USD&quot;) instead of including ambiguous symbols such as &#39;$&#39; in the value.  Use &#39;.&#39; (Unicode &#39;FULL STOP&#39; (U+002E)) rather than &#39;,&#39; to indicate a decimal point. Avoid using these symbols as a readability separator.  Note that both RDFa and Microdata syntax allow the use of a &quot;content=&quot; attribute for publishing simple machine-readable values alongside more human-friendly formatting.  Use values from 0123456789 (Unicode &#39;DIGIT ZERO&#39; (U+0030) to &#39;DIGIT NINE&#39; (U+0039)) rather than superficially similiar Unicode symbols. 

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'price'
    _expected_schema = None
    _enum = False
    _format_as = "DecimalField"


class priceSpecificationProp(SchemaProperty):

    """
    SchemaField for priceSpecification
    Usage: Include in SchemaObject SchemaFields as your_django_field = priceSpecificationProp()  
    schema.org description:One or more detailed price specifications, indicating the unit price and delivery or payment charges.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PriceSpecification"""

    _prop_schema = 'priceSpecification'
    _expected_schema = 'PriceSpecification'
    _enum = False
    _format_as = "ForeignKey"


# schema.org version 2.0
