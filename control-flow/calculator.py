# calculator.py(Module)
num1 = int(input(f"enter the first number: "))
num2 = int(input(f"enter the first number: "))
operation = input("Choose the operation (+, -, *, /): ")


def add(num1 , num2):
  """Returns the sum of two numbers."""
  return  num1 + num2

def subtract(x, y):
  """Returns the difference of two numbers."""
  return x - y

def multiplication(x, y):
    """Returns the multiplication of two numbers."""
    return x * y

def division(x ,y):
    """"Returns the division of the two number."""
    return x * y
  
if __name__ == "__main__":
    add()
    subtract()
    division()
    multiplication()
    