from factors import mass_conversion_factors, volume_conversion_factors, length_conversion_factors, temperature_units

def is_mass_unit(unit):
    return unit in mass_conversion_factors

def is_volume_unit(unit):
    return unit in volume_conversion_factors

def is_length_unit(unit):
    return unit in length_conversion_factors

def is_temperature_unit(unit):
    return unit in temperature_units