# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Place import isicV4Prop, openingHoursSpecificationProp, photoProp, reviewProp, telephoneProp, containedInProp, hasMapProp, aggregateRatingProp, additionalPropertyProp, addressProp, logoProp, faxNumberProp, geoProp, eventProp, globalLocationNumberProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class LandformSchema(SchemaObject):

    """Schema Mixin for Landform
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.
    """

    def __init__(self):
        self.schema = 'Landform'


# schema.org version 2.0
