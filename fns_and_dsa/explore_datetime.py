#def display_current_datetime():
   # current_date = display_current_datetime()
   # print(f"Current date and time: 2024-03-25 15:30:45 ")


#def calculate_future_date ():
 #   print(f"Enter the number of days to add to the current date:")
  #  future_date = calculate_future_date()
   # print(f"future days:")
   
# Timedelta function demonstration 
from datetime import datetime, timedelta

def display_current_datetime():
    global current_date
    current_date = display_current_datetime
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")
    

    
def calculate_future_date():
    future_date = calculate_future_date
    future_date = current_date + \
                         timedelta(days = int(input(f"Enter the number of days to add to the current date: ") ))
    #format the date as “YYYY-MM-DD”.
    print(f"future date: {future_date.strftime("%Y-%m-%d")} ") # print the formatted date 
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
