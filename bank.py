
from __future__ import with_statement


class Account:
    bank="standard _charter"
    def __init__(self,account_number,name):
        self.deposits=[]
        self.withdrawal=[]
        self.balance=0
        self.account_number=account_number
        self.name=name
    def deposit(self,amount):
        self.balance+=amount
        self.deposits.append(self.amount)
        return f"your deposit is{amount},the balance is {self.balance}"
         
    
    def withdraw(self,amount):
        self.amount=amount
        self.transaction_cost=100
        new_amount=amount+self.transaction_cost
        if amount>self.balance:
                return f'insufficient funds'
        elif amount<=0:
                 return f'Amount must be greater than zero'
        else:
          self.balance-=new_amount
          return f'hello{self.name} you have withdrawn{amount} your new balance is{self.balance}' 

    def deposits_statements(self):   
        print(""" Deposit Statement""")
        for deposit in self.deposits:
            print(f'your deposits was{deposit}')

    def withdrawal_statements(self):
        print(""" withdrawal Statement""")  
        for withdraw in self.withdrawal:
            print(f'your deposits was{withdraw}')

    def current_balance(self):
        return f"your current balance is{self.balance}"               



