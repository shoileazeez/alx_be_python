def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator) 
        result = numerator / denominator
        return f"The result of the division is {result}" 
    
    except ValueError:
         print(f"Error: Please enter numeric values only.")
    
    except ZeroDivisionError:
         print(f"Error: Cannot divide by zero.")
     
        
