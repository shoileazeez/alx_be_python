num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case '+':
        operation = num1 + num2
        print(f"The result is: {operation}")
    case '-':
        operation = num1 - num2
        print(f"The result is: {operation}")
    case '*':
        operation = num1 * num2 
        print(f"The result is: {operation}") 
    case '/':
        if num2 !=0:
            operation = num1 / num2
            print(f"The result is: {operation}")  
        else:
            print(f"cannot divide by zero .")