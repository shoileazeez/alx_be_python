#ef calculate_area(length, width):
    #"""Calculates the area of a rectangle."""
    #area = length * width
    #return area

# Passing argument
#calculate_area(10, 5)  # rectangle_area will be 50

#def user_info(name, age=None):
     #"""Prints user information."""
     #print(f"Name: {name}")
     #if age:
      #print(f"Age: {age}")
#user_info(name=input(f"enter your name: "), age=input(f"enter your age: "))


# Function definition with default value
#def greet(name=input(f"enter your name: ")):
     #"""Prints a greeting message."""
     #print(f"Hello, {name}!")
#greet()  # Output: Hello, World!
#greet("alice")  # Output: Hello, Alice! 


#def square(number):
 #"""Returns the square of a number."""
 #return number * number
#squared_value = square(4)  # squared_value will be 16

#count = input(f"enter your count: ")  # Global variable
#def increment():
     #count += 1  # This refers to the local count within the function
     #increment()
#print(count)  # Output: 0 (Global count remains unchanged)

#count = 0  # Global variable
#def increment():
     #count += 1  # This refers to the local count within the function
     #increment()
#print(count)  # Output: 0 (Global count remains unchanged)


#count = str(input(f"enter your count: "))
#def increment_global():
  #global count
  #count += 1
#increment_global()
#print(count)  # Output: 1 (Global count is modified)


#def outer_function():
    #x =float(input(f"enter the value of x: "))  # Variable in the enclosing function

    #def inner_function():
        #nonlocal x  # Using nonlocal to modify x from the enclosing function
        #x += 5  # Modifying the value of x

    #inner_function()  # Calling the nested function
    #print("Modified value of x from inner function:", x)
#outer_function()

#def add(x = float(input(f"enter the first number: ")) , y = float(input(f"enter the second number: "))):
  #"""Returns the sum of two numbers."""
  #return x + y
  
  
def perform_operation(num1, num2, operation):
     match operation:
          case"add":
               return num1 +num2
          case "subtract":
               return num1 - num2
          case "multiply":
               return num1 * num2
          case "divide":
               if num2 ==0:
                   return "error: division by zero"
               elif num1 == 0:
                  return "can not be divide by zero"
               else:
                  return num1 / num2
     
     
                 
     
               

               
    
     
      
