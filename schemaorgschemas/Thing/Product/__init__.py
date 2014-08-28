# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ProductSchema(SchemaObject):

    """Schema Mixin for Product
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.
    """

    def __init__(self):
        self.schema = 'Product'


class isConsumableForProp(SchemaProperty):

    """
    SchemaField for isConsumableFor
    Usage: Include in SchemaObject SchemaFields as your_django_field = isConsumableForProp()  
    schema.org description:A pointer to another product (or multiple products) for which this product is a consumable.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'isConsumableFor'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


class weightProp(SchemaProperty):

    """
    SchemaField for weight
    Usage: Include in SchemaObject SchemaFields as your_django_field = weightProp()  
    schema.org description:The weight of the product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'weight'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class isAccessoryOrSparePartForProp(SchemaProperty):

    """
    SchemaField for isAccessoryOrSparePartFor
    Usage: Include in SchemaObject SchemaFields as your_django_field = isAccessoryOrSparePartForProp()  
    schema.org description:A pointer to another product (or multiple products) for which this product is an accessory or spare part.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'isAccessoryOrSparePartFor'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


class colorProp(SchemaProperty):

    """
    SchemaField for color
    Usage: Include in SchemaObject SchemaFields as your_django_field = colorProp()  
    schema.org description:The color of the product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'color'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class brandProp(SchemaProperty):

    """
    SchemaField for brand
    Usage: Include in SchemaObject SchemaFields as your_django_field = brandProp()  
    schema.org description:The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Brand"""

    _prop_schema = 'brand'
    _expected_schema = 'Brand'
    _enum = False
    _format_as = "ForeignKey"


class gtin8Prop(SchemaProperty):

    """
    SchemaField for gtin8
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin8Prop()  
    schema.org description:The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin8'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class heightProp(SchemaProperty):

    """
    SchemaField for height
    Usage: Include in SchemaObject SchemaFields as your_django_field = heightProp()  
    schema.org description:The height of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'height'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class releaseDateProp(SchemaProperty):

    """
    SchemaField for releaseDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = releaseDateProp()  
    schema.org description:The release date of a product or product model. This can be used to distinguish the exact variant of a product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'releaseDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class isRelatedToProp(SchemaProperty):

    """
    SchemaField for isRelatedTo
    Usage: Include in SchemaObject SchemaFields as your_django_field = isRelatedToProp()  
    schema.org description:A pointer to another, somehow related product (or multiple products).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'isRelatedTo'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


class itemConditionProp(SchemaProperty):

    """
    SchemaField for itemCondition
    Usage: Include in SchemaObject SchemaFields as your_django_field = itemConditionProp()  
    schema.org description:A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference OfferItemCondition"""

    _prop_schema = 'itemCondition'
    _expected_schema = 'OfferItemCondition'
    _enum = False
    _format_as = "ForeignKey"


class logoProp(SchemaProperty):

    """
    SchemaField for logo
    Usage: Include in SchemaObject SchemaFields as your_django_field = logoProp()  
    schema.org description:A logo associated with an organization.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'logo'
    _expected_schema = None
    _enum = False
    _format_as = "URLField"


class manufacturerProp(SchemaProperty):

    """
    SchemaField for manufacturer
    Usage: Include in SchemaObject SchemaFields as your_django_field = manufacturerProp()  
    schema.org description:The manufacturer of the product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'manufacturer'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class productIDProp(SchemaProperty):

    """
    SchemaField for productID
    Usage: Include in SchemaObject SchemaFields as your_django_field = productIDProp()  
    schema.org description:The product identifier, such as ISBN. For example: &lt;meta itemprop=&#39;productID&#39; content=&#39;isbn:123-456-789&#39;/&gt;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'productID'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class skuProp(SchemaProperty):

    """
    SchemaField for sku
    Usage: Include in SchemaObject SchemaFields as your_django_field = skuProp()  
    schema.org description:The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'sku'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class isSimilarToProp(SchemaProperty):

    """
    SchemaField for isSimilarTo
    Usage: Include in SchemaObject SchemaFields as your_django_field = isSimilarToProp()  
    schema.org description:A pointer to another, functionally similar product (or multiple products).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Product"""

    _prop_schema = 'isSimilarTo'
    _expected_schema = 'Product'
    _enum = False
    _format_as = "TextField"


class aggregateRatingProp(SchemaProperty):

    """
    SchemaField for aggregateRating
    Usage: Include in SchemaObject SchemaFields as your_django_field = aggregateRatingProp()  
    schema.org description:The overall rating, based on a collection of reviews or ratings, of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference AggregateRating"""

    _prop_schema = 'aggregateRating'
    _expected_schema = 'AggregateRating'
    _enum = False
    _format_as = "ForeignKey"


class reviewProp(SchemaProperty):

    """
    SchemaField for review
    Usage: Include in SchemaObject SchemaFields as your_django_field = reviewProp()  
    schema.org description:A review of the item. Supercedes reviews.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Review"""

    _prop_schema = 'review'
    _expected_schema = 'Review'
    _enum = False
    _format_as = "ForeignKey"


class audienceProp(SchemaProperty):

    """
    SchemaField for audience
    Usage: Include in SchemaObject SchemaFields as your_django_field = audienceProp()  
    schema.org description:The intended audience of the item, i.e. the group for whom the item was created.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Audience"""

    _prop_schema = 'audience'
    _expected_schema = 'Audience'
    _enum = False
    _format_as = "ForeignKey"


class mpnProp(SchemaProperty):

    """
    SchemaField for mpn
    Usage: Include in SchemaObject SchemaFields as your_django_field = mpnProp()  
    schema.org description:The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'mpn'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class depthProp(SchemaProperty):

    """
    SchemaField for depth
    Usage: Include in SchemaObject SchemaFields as your_django_field = depthProp()  
    schema.org description:The depth of the product.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'depth'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class offersProp(SchemaProperty):

    """
    SchemaField for offers
    Usage: Include in SchemaObject SchemaFields as your_django_field = offersProp()  
    schema.org description:An offer to provide this item-for example, an offer to sell a product, rent the DVD of a movie, or give away tickets to an event.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Offer"""

    _prop_schema = 'offers'
    _expected_schema = 'Offer'
    _enum = False
    _format_as = "ForeignKey"


class gtin13Prop(SchemaProperty):

    """
    SchemaField for gtin13
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin13Prop()  
    schema.org description:The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin13'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class modelProp(SchemaProperty):

    """
    SchemaField for model
    Usage: Include in SchemaObject SchemaFields as your_django_field = modelProp()  
    schema.org description:The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'model'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class gtin14Prop(SchemaProperty):

    """
    SchemaField for gtin14
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin14Prop()  
    schema.org description:The GTIN-14 code of the product, or the product to which the offer refers.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin14'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class widthProp(SchemaProperty):

    """
    SchemaField for width
    Usage: Include in SchemaObject SchemaFields as your_django_field = widthProp()  
    schema.org description:The width of the item.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'width'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"
