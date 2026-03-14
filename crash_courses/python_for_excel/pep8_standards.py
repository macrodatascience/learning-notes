# Script Name: pep8_standards.py
print("1. Scripts should have a docstring at the beginning that describes its purpose and functionality.")

"""
This is a PEP 8 Sample Code showing the correct formatting and style guidelines for Python code. 
It includes examples of variable naming, function definitions, and class definitions

"""

print("""2. Importing necessary standard libraries on separate lines and grouped together at the top of the file.
    Third-party imports should be grouped together and placed after standard library imports.""")

import os
from pyclbr import Class
import sys
import datetime as dt

import numpy as np
import pandas as pd

print("3. Constants should be in uppercase with words separated by underscores.")

PI = 3.14159
TEMPERATURE_SCALES = ('Celsius', 'Fahrenheit', 'Kelvin')

print("""4. Class and Function definitions should be separated by two blank lines.
    The function names should be lowercase with words separated by underscores""")

print(""" 5. Class names should be in CamelCase and should not contain underscores. 
    Despite the fact that class names like datetime are in lowercase, it is generally recommended  
    to follow the CamelCase or CapitalizedWords convention for class names in your own code.""")

print("6. Inline comments should be separated by at least two spaces from the statement and should start with a # followed by a single space.")

class TemperatureConverter:
    pass  # Doesn't do anything yet just a placeholder for the class definition


print("7. Function definitions should use a lowercase name with words separated by underscores.")
print("8. Functions should have a docstring that describes the purpose of the function, its parameters, and its return value.")

print("9. Don't use spaces around the '=' sign when used to indicate a keyword argument or a default parameter value.")

print("10. Use spaces around math operators and after commas, but not directly inside parentheses, brackets, or braces.")

def convert_to_celsius(degrees, source='fahrenheit'):
    """Convert degrees Fahrenheit or Kelvin to the Celsius scale.
    """
    if source.lower() == 'fahrenheit':
        return (degrees - 32) * 5.0/9.0
    elif source.lower() == 'kelvin':
        return degrees - 273.15
    else:
        raise ValueError("Source must be 'fahrenheit' or 'kelvin'")
   
print("11. Use lowercases for variable names with words separated by underscores.")

celsius = convert_to_celsius(100, source='fahrenheit')

print("12. With slicing and indexing don't use spaces around the colon.")

non_celsius_scales = TEMPERATURE_SCALES[1:]  # Get the non-Celsius scales from the tuple