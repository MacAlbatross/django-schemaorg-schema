# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class ProductSchema(SchemaObject):

    """Schema Mixin for Product
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.
    """

    def __init__(self):
        self.schema = 'Product'


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
    schema.org description:The weight of the product or person.

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


class purchaseDateProp(SchemaProperty):

    """
    SchemaField for purchaseDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = purchaseDateProp()  
    schema.org description:The date the item e.g. vehicle was purchased by the current owner.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'purchaseDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class brandProp(SchemaProperty):

    """
    SchemaField for brand
    Usage: Include in SchemaObject SchemaFields as your_django_field = brandProp()  
    schema.org description:The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Organization"""

    _prop_schema = 'brand'
    _expected_schema = 'Organization'
    _enum = False
    _format_as = "ForeignKey"


class gtin8Prop(SchemaProperty):

    """
    SchemaField for gtin8
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin8Prop()  
    schema.org description:The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See GS1 GTIN Summary for more details.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin8'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class awardProp(SchemaProperty):

    """
    SchemaField for award
    Usage: Include in SchemaObject SchemaFields as your_django_field = awardProp()  
    schema.org description:An award won by or for this item. Supersedes awards.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'award'
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


class audienceProp(SchemaProperty):

    """
    SchemaField for audience
    Usage: Include in SchemaObject SchemaFields as your_django_field = audienceProp()  
    schema.org description:An intended audience, i.e. a group for whom something was created. Supersedes serviceAudience.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Audience"""

    _prop_schema = 'audience'
    _expected_schema = 'Audience'
    _enum = False
    _format_as = "ForeignKey"


class logoProp(SchemaProperty):

    """
    SchemaField for logo
    Usage: Include in SchemaObject SchemaFields as your_django_field = logoProp()  
    schema.org description:An associated logo.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference ImageObject"""

    _prop_schema = 'logo'
    _expected_schema = 'ImageObject'
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


class categoryProp(SchemaProperty):

    """
    SchemaField for category
    Usage: Include in SchemaObject SchemaFields as your_django_field = categoryProp()  
    schema.org description:A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'category'
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
    schema.org description:A review of the item. Supersedes reviews.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Review"""

    _prop_schema = 'review'
    _expected_schema = 'Review'
    _enum = False
    _format_as = "ForeignKey"


class additionalPropertyProp(SchemaProperty):

    """
    SchemaField for additionalProperty
    Usage: Include in SchemaObject SchemaFields as your_django_field = additionalPropertyProp()  
    schema.org description:A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference PropertyValue"""

    _prop_schema = 'additionalProperty'
    _expected_schema = 'PropertyValue'
    _enum = False
    _format_as = "ForeignKey"


class gtin14Prop(SchemaProperty):

    """
    SchemaField for gtin14
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin14Prop()  
    schema.org description:The GTIN-14 code of the product, or the product to which the offer refers. See GS1 GTIN Summary for more details.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin14'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class depthProp(SchemaProperty):

    """
    SchemaField for depth
    Usage: Include in SchemaObject SchemaFields as your_django_field = depthProp()  
    schema.org description:The depth of the item.

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
    schema.org description:An offer to provide this itemfor example, an offer to sell a product, rent the DVD of a movie, or give away tickets to an event.

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
    schema.org description:The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero. See GS1 GTIN Summary for more details.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin13'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class gtin12Prop(SchemaProperty):

    """
    SchemaField for gtin12
    Usage: Include in SchemaObject SchemaFields as your_django_field = gtin12Prop()  
    schema.org description:The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See GS1 GTIN Summary for more details.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'gtin12'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


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


class productionDateProp(SchemaProperty):

    """
    SchemaField for productionDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = productionDateProp()  
    schema.org description:The date of production of the item, e.g. vehicle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'productionDate'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


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


# schema.org version 2.0
