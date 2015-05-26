# -*- coding: utf-8 -*-
from schemaorgschemas.Thing import potentialActionProp, nameProp, sameAsProp, imageProp, urlProp, mainEntityOfPageProp, additionalTypeProp, alternateNameProp, descriptionProp
from schemaorgschemas.Thing.Product import isConsumableForProp, weightProp, isAccessoryOrSparePartForProp, colorProp, purchaseDateProp, gtin8Prop, heightProp, releaseDateProp, isRelatedToProp, logoProp, productIDProp, categoryProp, isSimilarToProp, reviewProp, audienceProp, widthProp, additionalPropertyProp, offersProp, productionDateProp, skuProp, mpnProp, brandProp, awardProp, itemConditionProp, manufacturerProp, aggregateRatingProp, gtin14Prop, depthProp, gtin13Prop, gtin12Prop, modelProp

from schemaorgschemas.djangoschema import SchemaObject, SchemaProperty, SchemaEnumProperty, SCHEMA_ORG
from django.conf import settings


class VehicleSchema(SchemaObject):

    """Schema Mixin for Vehicle
    Usage: place after django model in class definition, schema will return the schema.org url for the object
    A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.
    """

    def __init__(self):
        self.schema = 'Vehicle'


class numberOfDoorsProp(SchemaProperty):

    """
    SchemaField for numberOfDoors
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfDoorsProp()  
    schema.org description:The number of doors. Typical unit code(s): C62

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'numberOfDoors'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class numberOfAxlesProp(SchemaProperty):

    """
    SchemaField for numberOfAxles
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfAxlesProp()  
    schema.org description:The number of axles. Typical unit code(s): C62

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'numberOfAxles'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class vehicleTransmissionProp(SchemaProperty):

    """
    SchemaField for vehicleTransmission
    Usage: Include in SchemaObject SchemaFields as your_django_field = vehicleTransmissionProp()  
    schema.org description:The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) (&quot;gearbox&quot; for cars).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'vehicleTransmission'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class knownVehicleDamagesProp(SchemaProperty):

    """
    SchemaField for knownVehicleDamages
    Usage: Include in SchemaObject SchemaFields as your_django_field = knownVehicleDamagesProp()  
    schema.org description:A textual description of known damages, both repaired and unrepaired.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'knownVehicleDamages'
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


class vehicleSeatingCapacityProp(SchemaProperty):

    """
    SchemaField for vehicleSeatingCapacity
    Usage: Include in SchemaObject SchemaFields as your_django_field = vehicleSeatingCapacityProp()  
    schema.org description:The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law. Typical unit code(s): C62 for persons

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'vehicleSeatingCapacity'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class vehicleIdentificationNumberProp(SchemaProperty):

    """
    SchemaField for vehicleIdentificationNumber
    Usage: Include in SchemaObject SchemaFields as your_django_field = vehicleIdentificationNumberProp()  
    schema.org description:The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'vehicleIdentificationNumber'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class steeringPositionProp(SchemaProperty):

    """
    SchemaField for steeringPosition
    Usage: Include in SchemaObject SchemaFields as your_django_field = steeringPositionProp()  
    schema.org description:The position of the steering wheel or similar device (mostly for cars).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference SteeringPositionValue"""

    _prop_schema = 'steeringPosition'
    _expected_schema = 'SteeringPositionValue'
    _enum = False
    _format_as = "ForeignKey"


class numberOfForwardGearsProp(SchemaProperty):

    """
    SchemaField for numberOfForwardGears
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfForwardGearsProp()  
    schema.org description:The total number of forward gears available for the transmission system of the vehicle. Typical unit code(s): C62

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'numberOfForwardGears'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class fuelConsumptionProp(SchemaProperty):

    """
    SchemaField for fuelConsumption
    Usage: Include in SchemaObject SchemaFields as your_django_field = fuelConsumptionProp()  
    schema.org description:The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km). Note 1: There are unfortunately no standard unit codes for liters per 100 km. Use unitText to indicate the unit of measurement, e.g. L/100 km. Note 2: There are two ways of indicating the fuel consumption, fuelConsumption (e.g. 8 liters per 100 km) and fuelEfficiency (e.g. 30 miles per gallon). They are reciprocal. Note 3: Often, the absolute value is useful only when related to driving speed (&quot;at 80 km/h&quot;) or usage pattern (&quot;city traffic&quot;). You can use valueReference to link the value for the fuel consumption to another value.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'fuelConsumption'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class vehicleInteriorColorProp(SchemaProperty):

    """
    SchemaField for vehicleInteriorColor
    Usage: Include in SchemaObject SchemaFields as your_django_field = vehicleInteriorColorProp()  
    schema.org description:The color or color combination of the interior of the vehicle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'vehicleInteriorColor'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class driveWheelConfigurationProp(SchemaProperty):

    """
    SchemaField for driveWheelConfiguration
    Usage: Include in SchemaObject SchemaFields as your_django_field = driveWheelConfigurationProp()  
    schema.org description:The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle&#39;s engine via the drivetrain.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'driveWheelConfiguration'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class vehicleEngineProp(SchemaProperty):

    """
    SchemaField for vehicleEngine
    Usage: Include in SchemaObject SchemaFields as your_django_field = vehicleEngineProp()  
    schema.org description:Information about the engine or engines of the vehicle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference EngineSpecification"""

    _prop_schema = 'vehicleEngine'
    _expected_schema = 'EngineSpecification'
    _enum = False
    _format_as = "ForeignKey"


class fuelTypeProp(SchemaProperty):

    """
    SchemaField for fuelType
    Usage: Include in SchemaObject SchemaFields as your_django_field = fuelTypeProp()  
    schema.org description:The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'fuelType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class cargoVolumeProp(SchemaProperty):

    """
    SchemaField for cargoVolume
    Usage: Include in SchemaObject SchemaFields as your_django_field = cargoVolumeProp()  
    schema.org description:The available volume for cargo or luggage. For automobiles, this is usually the trunk volume. Typical unit code(s): LTR for liters, FTQ for cubic foot/feet Note: You can use minValue and maxValue to indicate ranges.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'cargoVolume'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class vehicleModelDateProp(SchemaProperty):

    """
    SchemaField for vehicleModelDate
    Usage: Include in SchemaObject SchemaFields as your_django_field = vehicleModelDateProp()  
    schema.org description:The release date of a vehicle model (often used to differentiate versions of the same make and model).

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference Date"""

    _prop_schema = 'vehicleModelDate'
    _expected_schema = 'Date'
    _enum = False
    _format_as = "ForeignKey"


class numberOfAirbagsProp(SchemaProperty):

    """
    SchemaField for numberOfAirbags
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfAirbagsProp()  
    schema.org description:The number or type of airbags in the vehicle.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'numberOfAirbags'
    _expected_schema = None
    _enum = False
    _format_as = "FloatField"


class vehicleInteriorTypeProp(SchemaProperty):

    """
    SchemaField for vehicleInteriorType
    Usage: Include in SchemaObject SchemaFields as your_django_field = vehicleInteriorTypeProp()  
    schema.org description:The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'vehicleInteriorType'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class fuelEfficiencyProp(SchemaProperty):

    """
    SchemaField for fuelEfficiency
    Usage: Include in SchemaObject SchemaFields as your_django_field = fuelEfficiencyProp()  
    schema.org description:The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L). Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use unitText to indicate the unit of measurement, e.g. mpg or km/L. Note 2: There are two ways of indicating the fuel consumption, fuelConsumption (e.g. 8 liters per 100 km) and fuelEfficiency (e.g. 30 miles per gallon). They are reciprocal. Note 3: Often, the absolute value is useful only when related to driving speed (&quot;at 80 km/h&quot;) or usage pattern (&quot;city traffic&quot;). You can use valueReference to link the value for the fuel economy to another value.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'fuelEfficiency'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


class vehicleConfigurationProp(SchemaProperty):

    """
    SchemaField for vehicleConfiguration
    Usage: Include in SchemaObject SchemaFields as your_django_field = vehicleConfigurationProp()  
    schema.org description:A short text indicating the configuration of the vehicle, e.g. &#39;5dr hatchback ST 2.5 MT 225 hp&#39; or &#39;limited edition&#39;.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'vehicleConfiguration'
    _expected_schema = None
    _enum = False
    _format_as = "TextField"


class dateVehicleFirstRegisteredProp(SchemaProperty):

    """
    SchemaField for dateVehicleFirstRegistered
    Usage: Include in SchemaObject SchemaFields as your_django_field = dateVehicleFirstRegisteredProp()  
    schema.org description:The date of the first registration of the vehicle with the respective public authorities.

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'dateVehicleFirstRegistered'
    _expected_schema = None
    _enum = False
    _format_as = "DateField"


class numberOfPreviousOwnersProp(SchemaProperty):

    """
    SchemaField for numberOfPreviousOwners
    Usage: Include in SchemaObject SchemaFields as your_django_field = numberOfPreviousOwnersProp()  
    schema.org description:The number of owners of the vehicle, including the current one. Typical unit code(s): C62

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    """

    _prop_schema = 'numberOfPreviousOwners'
    _expected_schema = None
    _enum = False
    _format_as = "IntegerField"


class mileageFromOdometerProp(SchemaProperty):

    """
    SchemaField for mileageFromOdometer
    Usage: Include in SchemaObject SchemaFields as your_django_field = mileageFromOdometerProp()  
    schema.org description:The total distance travelled by the particular vehicle since its initial production, as read from its odometer. Typical unit code(s): KMT for kilometers, SMI for statute miles

    prop_schema returns just the property without url#
    format_as is used by app templatetags based upon schema.org datatype
    used to reference QuantitativeValue"""

    _prop_schema = 'mileageFromOdometer'
    _expected_schema = 'QuantitativeValue'
    _enum = False
    _format_as = "IntegerField"


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


# schema.org version 2.0
