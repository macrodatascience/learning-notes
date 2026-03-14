TEMPERATURE_SCALES = ('Celsius', 'Fahrenheit', 'Kelvin')

def convert_to_celsius(degrees, source='fahrenheit'):
    """Convert degrees Fahrenheit or Kelvin to the Celsius scale.
    """
    if source.lower() == 'fahrenheit':
        return (degrees - 32) * 5.0/9.0
    elif source.lower() == 'kelvin':
        return degrees - 273.15
    else:
        raise ValueError("Source must be 'fahrenheit' or 'kelvin'")
    
print("This is the temperature module that provides a function to convert temperatures to Celsius from either Fahrenheit or Kelvin scales.")

if __name__ == "__main__":
    # Example usage of the convert_to_celsius function
    temp_f = 100
    temp_k = 373.15
    
    print(f"{temp_f} degrees Fahrenheit is equal to {convert_to_celsius(temp_f, source='fahrenheit')} degrees Celsius.")
    print(f"{temp_k} degrees Kelvin is equal to {convert_to_celsius(temp_k, source='kelvin')} degrees Celsius.")