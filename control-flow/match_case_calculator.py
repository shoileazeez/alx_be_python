num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
Choose_the_operation = input("Choose the operation (+, -, *, /): ")

match Choose_the_operation:
    case '+':
        Choose_the_operation = num1 + num2
        print(f"The result is :{Choose_the_operation}")
    case '-':
        Choose_the_operation = num1 - num2
        print(f"The result is :{Choose_the_operation}")
    case '*':
        Choose_the_operation = num1 * num2 
        print(f"The result is :{Choose_the_operation}") 
    case '/':
        if num2 !=0:
            Choose_the_operation = num1 / num2
            print(f"The result is :{Choose_the_operation}")  
        else:
            print(f"cannot divide by zero .")
                