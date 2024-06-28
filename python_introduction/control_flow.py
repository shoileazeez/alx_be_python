#age = int(input("Enter your age: "))

#if age >= 18:
#    print("You are eligible to vote.")
    
#else:
#    print("You are not eligible to vote yet.")

#purchase_amount = float(input("Enter your purchase amount: "))

#if purchase_amount >= 1000:
 # discount = 0.1  # 10% discount
#elif purchase_amount >= 500:
 # discount = 0.05  # 5% discount
#else:
  #discount = 0  # No discount
  
#final_price = purchase_amount * (1 - discount)
#print("Final price after discount: $" + str(final_price))

score = int(input("Enter your score: "))

if score >= 90:
  grade = "A"
elif score >= 80:
  grade = "B"
elif score >= 70:
  grade = "C"
else:
  grade = "F"
print("Your grade is:", grade)


#day = input("Enter a day of the week (Monday-Sunday): ").lower()

#match day:
    #case "monday":
        #print("Ugh, Mondays...")
    #case "tuesday":
        #print("Just another workday...")
    #case "wednesday":
        #print("Hump day!")
    #case "thursday":
        #print("Almost there...")
    #case "friday":
        #print("TGIF!")
    #case "saturday" | "sunday":  # Match multiple values with pipe (|)
        #print("Weekend vibes!")
    #case _:
        #print("Invalid day entered.")
        
value = input("Enter a value (number or string): ")

match value:
    case int():
        print("You entered an integer:", value)
    case str():
        print("You entered a string:", value)
    case _:
        print("Invalid data type entered.")


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)
  
  age = 0

while age < 18:
  age = int(input("Enter your age (must be 18 or older): "))

print("You are old enough to proceed.")
    
age = 0

while age < 18:
  age = int(input("Enter your age (must be 18 or older): "))

print("You are old enough to proceed.")

secret_number = 7

guess_count = 0
guess = 0

while guess != secret_number:
  guess_count += 1
  guess = int(input("Guess a number between 1 and 10: "))

print(f"You guessed it in {guess_count} tries!")

shopping_list = ["apples", "bread", "milk", "cheese"]
item_found = False

while not item_found:
  item = input("Search for an item in your list (or 'q' to quit): ")
  if item.lower() == "q":
    break  # Exit the loop if user enters 'q'
  if item in shopping_list:
    item_found = True
    print(f"{item} is on your shopping list.")
  else:
    print(f"{item} is not on your list.")
    
    
rows = 5

for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    print("*", end="")
    
  print()  # Move to a new line after each row of asterisks    
for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    product = i * j
    print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
  print()  # Move to a new line after each row  