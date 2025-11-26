import sys
from factors import mass_conversion_factors, length_conversion_factors, volume_conversion_factors, temperature_units, ingredient_density_data
from ingredients import Ingredient, is_mass_unit, is_length_unit, is_temperature_unit, is_volume_unit
from string_parse import INGREDIENT_PARSE_PATTERN, parse_ingredient_string

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ingredient_string = sys.argv[1]
        value, unit, name = parse_ingredient_string(ingredient_string)
    
    if value is not None:
        my_ingredient = Ingredient(name = name, value = value, unit = unit)
        print(f"Parsed Ingredient {my_ingredient.value} {my_ingredient.unit} {my_ingredient.name}")

        if my_ingredient.unit in mass_conversion_factors:
            print(f"Converting {my_ingredient.value}{my_ingredient.unit} to kg...")
            my_ingredient.convert_to("kg")
            print(f"Converted: {my_ingredient.value}{my_ingredient.unit} {my_ingredient.name}")
        
        elif my_ingredient.unit in volume_conversion_factors:
            print(f"Converting {my_ingredient.value}{my_ingredient.unit} to ml...")
            my_ingredient.convert_to("ml")
            print(f"Converted: {my_ingredient.value}{my_ingredient.unit} {my_ingredient.name}")

         # Add more conversion examples here...
        else:
            print(f"Error: Could not parse '{ingredient_string}'. Please check the format.")
    else:
        print("Usage: python your_script_name.py \"<ingredient string>\"")    