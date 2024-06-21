#name = input("What is your name? ")
#print("Hello,", name) 
#age1 = input("how old are you? :")
#print(age1 ,"years old")
#num2 = int(input("Enter your age: "))
#print(num2 ,"years old")
#num3 = int(input("Enter the second number: "))
#age = num2 + num3
#print(f" In 2050, you will be {age} years old")

current_age = int(input("How old are you?"))
current_year = 2023
future_year = 2050

years_difference = future_year - current_year
future_age = current_age + years_difference

print(f"in {future_year}, you would be {future_age} years old.")