import re

INGREDIENT_PARSE_PATTERN = re.compile(r"^(\d+\s*\d*\/\s*\d+|\d+(?:\.\d+)?)\s*([a-zA-Z_]+)\s*(.*)$")

def parse_ingredient_string(text):
    match = INGREDIENT_PARSE_PATTERN.match(text.strip())
    
    if match:
        value_str = match.group(1).strip()
        unit = match.group(2).strip().lower()
        name = match.group(3).strip.lower()

        if "/" in value_str:
            num, den = map(int, value_str.split('/'))
            value = num/den
        else:
            value = float(value_str)
        return value_str, unit, name
    
    else:
        print(f"Warning: Could not parse '{text}'")
        return None, None ,None