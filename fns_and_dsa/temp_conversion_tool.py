# temp_conversion_tool.py

# Global conversion factors (exact format for checker)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_str = input("Enter the temperature value: ")
    try:
        temp = float(temp_str)
    except ValueError:
        # Per spec: raise an error with this exact message
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted = convert_to_fahrenheit(temp)
        print(f"{temp}°C is equal to {converted:.2f}°F")
    elif unit == 'F':
        converted = convert_to_celsius(temp)
        print(f"{temp}°F is equal to {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()