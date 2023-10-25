def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

while True:
    print("Choose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Quit")

    choice = input("Enter the option (1/2/3/4/5/6/7): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    elif choice == '3':
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius_to_kelvin(celsius)
        print(f"{celsius}°C is equal to {kelvin} K")
    elif choice == '4':
        kelvin = float(input("Enter temperature in Kelvin: "))
        celsius = kelvin_to_celsius(kelvin)
        print(f"{kelvin} K is equal to {celsius}°C")
    elif choice == '5':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        print(f"{fahrenheit}°F is equal to {kelvin} K")
    elif choice == '6':
        kelvin = float(input("Enter temperature in Kelvin: "))
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        print(f"{kelvin} K is equal to {fahrenheit}°F")
    elif choice == '7':
        break
    else:
        print("Invalid option. Please enter a valid option (1/2/3/4/5/6/7).")
