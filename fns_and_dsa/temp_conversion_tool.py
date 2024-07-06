#FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 
#CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


#def convert_to_celsius(fahrenheit):
  #  global FAHRENHEIT_TO_CELSIUS_FACTOR
   # if isinstance(fahrenheit,(int, float)):
    #    celsius = (fahrenheit -32) * CELSIUS_TO_FAHRENHEIT_FACTOR
     #   return celsius
    #else:
     #   raise ValueError("Invalid temperature. please enter: ")
    

#def convert_to_fahrenheit(celsius):
 #   global CELSIUS_TO_FAHRENHEIT_FACTOR
  ##  if isinstance(celsius, (int, float)):
    # fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR + 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    #return fahrenheit
    
#def main():
 #   while True:
  #      try:
   #         temperature = float(input("Enter the temperature: "))
    #        unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").upper()

#            match unit:
 #               case "C":
  #                  converted_temperature = convert_to_fahrenheit(temperature)
   #                 print(f"{temperature}°C is {converted_temperature}°F")
    #            case "F":
     #               converted_temperature = convert_to_celsius(temperature)
      #              print(f"{temperature}°F is {converted_temperature}°C")
       #         case _:
        #            print("Invalid input. Please enter 'C' or 'F'.")

        #except ValueError as e:
          #  print(str(e))
          #  continue

        #choice = input("Do you want to convert another temperature? (y/n): ").lower()
        #if choice != 'y':
         #   print("Exiting the temperature conversion tool.")
          #  break

#if __name__ == "__main__":
 #   main()    
 
 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

#Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    if isinstance(fahrenheit, (int, float)):
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

#Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    if isinstance(celsius, (int, float)):
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return fahrenheit
    else:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

#Main function for user interaction
def main():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            unit = input("Is the temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit == 'C':
                converted_temperature = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temperature}°F")
            elif unit == 'F':
                converted_temperature = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temperature}°C")
            else:
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
 
     

                 
                
                    
    