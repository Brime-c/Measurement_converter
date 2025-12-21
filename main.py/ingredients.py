from factors import mass_conversion_factors, length_conversion_factors, volume_conversion_factors, temperature_units, ingredient_density_data
from helpers import is_mass_unit, is_length_unit, is_temperature_unit, is_volume_unit


class Ingredient:
    def __init__(self, name, value, unit):
        self.name = name
        self.value = value
        self.unit = unit
    
    def convert_to(self, target_unit):
        if is_mass_unit(self.unit) and is_mass_unit(target_unit):
            first_step = self.value * mass_conversion_factors[self.unit]
            second_step = first_step / mass_conversion_factors[target_unit]
            self.value = round(second_step, 2)
            self.unit = target_unit
        elif is_volume_unit(self.unit) and is_volume_unit(target_unit):
            first_step = self.value * volume_conversion_factors[self.unit]
            second_step = first_step / volume_conversion_factors[target_unit]
            self.value = round(second_step, 2)
            self.unit = target_unit
        elif is_length_unit(self.unit) and is_length_unit(target_unit):
            first_step = self.value * length_conversion_factors[self.unit]
            second_step = first_step / length_conversion_factors[target_unit]
            self.value = round(second_step, 2)
            self.unit = target_unit
        elif is_temperature_unit(self.unit) and is_temperature_unit(target_unit):
            if target_unit == "celsius":
                self.to_celsius()
            elif target_unit == "fahrenheit":
                self.to_fahrenheit()
            elif target_unit == "kelvin":
                self.to_kelvin()
        elif is_mass_unit(self.unit) and is_volume_unit(target_unit):
            if self.name in ingredient_density_data:
                value_in_grams = self.value * mass_conversion_factors[self.unit]
                value_in_cups = value_in_grams / ingredient_density_data[self.name]
                value_in_ml_base = value_in_cups * volume_conversion_factors["cup"]
                final_value = value_in_ml_base / volume_conversion_factors[target_unit]
                self.value = round(final_value, 2)
                self.unit = target_unit
        elif is_volume_unit(self.unit) and is_mass_unit(target_unit):
            if self.name in ingredient_density_data:
                value_in_ml = self.value * volume_conversion_factors[self.unit]
                value_in_cups = value_in_ml / volume_conversion_factors["cup"]
                value_in_grams_base = value_in_cups * ingredient_density_data[self.name]
                final_value = value_in_grams_base / mass_conversion_factors[target_unit]
                self.value = round(final_value, 2)
                self.unit = target_unit
        else:
            raise Exception ("Not a valid conversion")

    def to_fahrenheit(self):
        if self.unit == "celsius":
            converted = (self.value * 1.8) + 32
        elif self.unit == "kelvin":
            preconverted = (self.value - 273.15)
            converted = (preconverted * 1.8) + 32
        elif self.unit == "fahrenheit":
            converted = self.value
        else:
            raise Exception ("Unit not supported")
        self.unit = "fahrenheit"
        self.value = round(converted, 2)
    
    def to_celsius(self):
        if self.unit == "fahrenheit":
            converted = (self.value - 32) / 1.8
        elif self.unit == "kelvin":
            converted = self.value - 273.15
        elif self.unit == "celsius":
            converted = self.value
        else:
            raise Exception ("Unit not supported")
        self.unit = "celsius"
        self.value = round(converted, 2)
    
    def to_kelvin(self):
        if self.unit == "celsius":
            converted = self.value + 273.15
        elif self.unit == "fahrenheit":
            pre_converted = (self.value - 32) / 1.8
            converted = pre_converted + 273.15
        elif self.unit == "kelvin":
            converted = self.value
        else:
            raise Exception ("Unit not supported")
        self.unit = "kelvin"
        self.value = round(converted, 2)