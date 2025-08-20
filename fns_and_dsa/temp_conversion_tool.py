git add temp_conversion_tool.pygit commit -m "Add user interaction to temp_conversion_tool.py"git push origin master   # or master, depending on branch# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # 👇 Required exact prompts
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
        elif unit == "F":
            print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
