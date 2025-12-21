import sys
from ingredients import Ingredient
from string_parse import INGREDIENT_PARSE_PATTERN, parse_ingredient_string


if __name__ == "__main__":
    # Expecting 3 arguments: script_name, ingredient_string, target_unit
    if len(sys.argv) == 3:
        ingredient_string = sys.argv[1]
        target_conversion_unit = sys.argv[2].lower() # Convert target unit to lowercase for consistency
        
        value, unit, name = parse_ingredient_string(ingredient_string)

        if value is not None:
            my_ingredient = Ingredient(name=name, value=value, unit=unit)
            
            print(f"Original: {my_ingredient.value} {my_ingredient.unit} {my_ingredient.name}")
            
            try:
                my_ingredient.convert_to(target_conversion_unit)
                print(f"Converted: {my_ingredient.value} {my_ingredient.unit} {my_ingredient.name}")
            except Exception as e:
                print(f"Conversion Error: {e}")
            
        else:
            print(f"Error: Could not parse ingredient '{ingredient_string}'. Please check the format.")
    else:
        print("Usage: python your_script_name.py \"<ingredient string>\" <target_unit>")
        print("Example: python your_script_name.py \"2.5 cups flour\" ml")
        print("Example: python your_script_name.py \"1/2 tsp salt\" g")
        print("Example: python your_script_name.py \"20 celsius water\" fahrenheit")