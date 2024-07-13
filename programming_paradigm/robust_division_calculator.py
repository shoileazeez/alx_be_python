def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator) 
        result = numerator / denominator
        return f"The result of the division is {result}" 
    
    except ValueError:
         raise ValueError("Error: please enter the numeric value ") from None
    
    except ZeroDivisionError:
         raise ZeroDivisionError
     
        
