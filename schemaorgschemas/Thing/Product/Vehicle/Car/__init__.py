# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, descriptionProp, urlProp, imageProp, sameAsProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, nameProp
from schemaorgschemas.Thing.Product import isConsumableForProp, weightProp, isAccessoryOrSparePartForProp, colorProp, purchaseDateProp, gtin8Prop, heightProp, releaseDateProp, isRelatedToProp, logoProp, productIDProp, categoryProp, isSimilarToProp, reviewProp, audienceProp, widthProp, additionalPropertyProp, offersProp, productionDateProp, skuProp, mpnProp, brandProp, awardProp, itemConditionProp, manufacturerProp, aggregateRatingProp, gtin14Prop, depthProp, gtin13Prop, gtin12Prop, modelProp
from schemaorgschemas.Thing.Product.Vehicle import numberOfDoorsProp, vehicleTransmissionProp, purchaseDateProp, vehicleSeatingCapacityProp, driveWheelConfigurationProp, vehicleEngineProp, fuelTypeProp, cargoVolumeProp, numberOfAirbagsProp, vehicleConfigurationProp, dateVehicleFirstRegisteredProp, numberOfPreviousOwnersProp, productionDateProp, numberOfAxlesProp, knownVehicleDamagesProp, vehicleIdentificationNumberProp, steeringPositionProp, numberOfForwardGearsProp, fuelConsumptionProp, vehicleInteriorColorProp, vehicleInteriorTypeProp, fuelEfficiencyProp, mileageFromOdometerProp, vehicleModelDateProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class CarSchema(SchemaObject):

    """Schema Mixin for Car
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A car is a wheeled, self-powered motor vehicle used for transportation.
    """

    def __init__(self):
        self.schema = 'Car'


# schema.org version 2.0
