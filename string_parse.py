import re
from unit_aliases import unit_aliases
from ingredients import Ingredient, is_mass_unit, is_length_unit, is_temperature_unit, is_volume_unit

INGREDIENT_PARSE_PATTERN = re.compile(r"^(\d+\s*\d*\/\s*\d+|\d+(?:\.\d+)?)\s*([a-zA-Z_]+)(?:\s+of)?\s*(.*)$")

def parse_ingredient_string(text):
    match = INGREDIENT_PARSE_PATTERN.match(text.strip())
    
    if match:
        value_str = match.group(1).strip()
        pre_unit = match.group(2).strip().lower()
        name = match.group(3).strip().lower()

        unit = unit_aliases.get(pre_unit, pre_unit)
        if not (is_mass_unit(unit) or is_volume_unit(unit) or is_length_unit(unit) or is_temperature_unit(unit)):
            raise ValueError(f"'{unit}' is not a recognized or convertible unit.")
        
        if "/" in value_str:
            num, den = map(int, value_str.split('/'))
            value = num/den
        else:
            value = float(value_str)
        return value, unit, name
    
    else:
        print(f"Warning: Could not parse '{text}'")
        return None, None ,None
    
if __name__ == "__main__":
    test_inputs = [
        "2 cups of flour",
        "1.5 cups sugar",
        "1/2 cup milk",
        "350g butter",
        "100ml water",
        "250 C oven", # Test temperature and unit abbreviation
        "1 kilogram all-purpose flour",
        "500 ml juice",
        "3 tsp salt",
        "1 tbsp oil",
        "0.75 lb beef", # Test float with imperial mass
        "25 mm ginger",
        "1 inch vanilla bean",
        "50 degF water", # Another temperature test
        "3.0 l soda",
        "2 eggs", # Should warn or return None if unit is missing
        "2 cups", # What if name is missing?
        "invalid string format", # Completely unparseable
    ]

    print("--- Testing parse_ingredient_string ---")
    for input_str in test_inputs:
        print(f"\nParsing: '{input_str}'")
        value, unit, name = parse_ingredient_string(input_str)
        if value is not None:
            print(f"  Parsed -> Value: {value}, Unit: '{unit}', Name: '{name}'")
        else:
            print(f"  Parsing failed (returned None).")

