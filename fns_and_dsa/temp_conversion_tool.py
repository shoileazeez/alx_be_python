FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    if isinstance(FAHRENHEIT_TO_CELSIUS_FACTOR,(int, float)):
        FAHRENHEIT_TO_CELSIUS_FACTOR = (FAHRENHEIT_TO_CELSIUS_FACTOR -32) * CELSIUS_TO_FAHRENHEIT_FACTOR
        return FAHRENHEIT_TO_CELSIUS_FACTOR
    else:
        raise ValueError("Invalid temperature. please enter: ")
    

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    if isinstance(CELSIUS_TO_FAHRENHEIT_FACTOR, (int, float)):
        CELSIUS_TO_FAHRENHEIT_FACTOR = (CELSIUS_TO_FAHRENHEIT_FACTOR + 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return CELSIUS_TO_FAHRENHEIT_FACTOR
    
def main():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").upper()

            match unit:
                case "C":
                    converted_temperature = convert_to_fahrenheit(temperature)
                    print(f"{temperature}°C is {converted_temperature}°F")
                case "F":
                    converted_temperature = convert_to_celsius(temperature)
                    print(f"{temperature}°F is {converted_temperature}°C")
                case _:
                    print("Invalid input. Please enter 'C' or 'F'.")

        except ValueError as e:
            print(str(e))
            continue

        choice = input("Do you want to convert another temperature? (y/n): ").lower()
        if choice != 'y':
            print("Exiting the temperature conversion tool.")
            break

if __name__ == "__main__":
    main()    
     

                 
                
                    
    