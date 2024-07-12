# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class BankAccount:
  def __init__(self,initial_balance = 0):
      self.account_balance = initial_balance
      
  def  deposit(self, amount):
        # amount = input(float(f"enter the amount you will like to deposit: "))
        self.account_balance += amount
        return self.account_balance
  def withdraw(self, amount): 
        # amount = input(float(f"enter the amount you would like to withdraw: "))
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        else:
            return False
  def display_balance(self):
      print(f"Current Balance: {self.account_balance:.2f} ")
  
           
            
            
          
            