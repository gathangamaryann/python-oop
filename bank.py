
class Account:
    bank="standard _charter"
    def __init__(self,balance,account_number):
        self.balance=balance
        self.account_number=account_number 
        
def deposit(self,amount):
    self.amount=amount
    self.balance+=amount
    return self.balance
    return f"Your deposit is {amount} in account{self.account_number}. The balance is {self.balance}"


def withdraw(self,amount):
    self.amount=amount
    self.withdraw-=amount
    return self.balance
    return f"Your withdrawal is {amount} in account{self.account_number}. The balance is {self.balance}"    