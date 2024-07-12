#assign & compute variables
#Global conversion factors
#FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
#CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

#Function to convert Fahrenheit to Celsius
#def convert_to_celsius(fahrenheit):
 #   global FAHRENHEIT_TO_CELSIUS_FACTOR
  #  if isinstance(fahrenheit, (int, float)):
   #     celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    #    return celsius
   # else:
    #    raise ValueError("Invalid temperature. Please enter a numeric value.")

#Function to convert Celsius to Fahrenheit
#def convert_to_fahrenheit(celsius):
 #   global CELSIUS_TO_FAHRENHEIT_FACTOR
    #if isinstance(celsius, (int, float)):
       # fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
       # return fahrenheit
   # else:
       # raise ValueError("Invalid temperature. Please enter a numeric value.")

#Main function for user interaction
#def main():
   # while True:
      #  try:
          #  temperature = float(input("Enter the temperature to convert: "))
         #   unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

           # match unit :
               # case 'C':
               #  converted_temperature = convert_to_fahrenheit(temperature)
                # print(f"{temperature}°C is {converted_temperature}°F")
                 
                #case'F':
                # converted_temperature = convert_to_celsius(temperature)
                # print(f"{temperature}°F is {converted_temperature}°C")
                 
                #case _ :
                # print("Invalid input. Please enter 'C' or 'F'.")

       # except ValueError as e:
          #  print(str(e))
           # continue

        #choice = input("Do you want to convert another temperature? (y/n): ").lower()
       # if choice != 'y':
       #     print("Exiting the temperature conversion tool.")
        #    break

#if __name__ == "__main__":
    #main()
    
# dfrom arithmetic_operations import perform_operation
from arithmetic_operations import perform_operation
def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()