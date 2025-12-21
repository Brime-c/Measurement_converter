# Measurement_converter

This is a simple yet robust measurement converter, developed as my first personal project during the Boot.dev programming course. The primary goal is to provide an easy-to-use tool for converting ingredient measurements commonly found in recipes, handling various units and even ingredient-specific density conversions.

## Features

*   Converts between various **mass units** (e.g., grams, kilograms, pounds, ounces).
*   Converts between various **volume units** (e.g., milliliters, liters, cups, tablespoons, fluid ounces).
*   Converts between various **length units** (e.g., inches, centimeters, millimeters) for specific ingredient dimensions.
*   Converts between **temperature units** (Celsius, Fahrenheit, Kelvin).
*   Handles **ingredient-specific mass-to-volume and volume-to-mass conversions** (e.g., converting grams of flour to cups of flour) using a density database.
*   Parses natural language input, including fractions and decimals, and normalizes unit aliases (e.g., "cups" to "cup", "tsp" to "us_tsp").

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Brime/Measurement_converter.git # Replace with your actual repo URL
    cd Measurement_converter
    ```
2.  **Run the converter from your terminal:**
    Use the `converter.py` script, providing the ingredient string and the target unit. Remember to wrap the ingredient string in quotes if it contains spaces.

    **Syntax:** `python3 converter.py "<value unit ingredient_name>" <target_unit>`

    **Examples:**
    ```bash
    python3 converter.py "2 cups of water" ml          # Convert 2 cups of water to milliliters
    python3 converter.py "1/2 tsp salt" g              # Convert half a teaspoon of salt to grams
    python3 converter.py "20 celsius water" fahrenheit # Convert 20 Celsius water to Fahrenheit
    python3 converter.py "1 lb butter" kg              # Convert 1 pound of butter to kilograms
    python3 converter.py "200g sugar" cup             # Convert 200 grams of sugar to cups (mass-to-volume)
    python3 converter.py "50 ml milk" oz               # Convert 50 ml of milk to ounces (volume-to-mass)
    python3 converter.py "10 inch board" cm            # Convert 10 inches to centimeters
    ```