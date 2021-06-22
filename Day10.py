class Bank_Acc:
    def __init__(self):
        self.balance=0
        print("Welcome to ATM MACHINE")
    def display(self):
        print()
        print("YOUR ACCOUNT BALANCE: ",self.balance)

class ADDING(Bank_Acc):  
    def deposit(self):
        amount=int(input("Enter RUPEES to be added : "))
        self.balance += amount
        print()
        print("Amount Deposited:",amount)
class WITHDRAWING(Bank_Acc):  
    def withdraw(self):
        amount = int(input("Enter RUPEES to be Withdrawn : "))
        if self.balance>=amount:
            self.balance-=amount
            print()
            print(" You Withdrew:", amount)
        else:
            print()
            print("Insufficient balance  ")
s = Bank_Acc()
p=ADDING()
p.deposit()

q=WITHDRAWING()
q.withdraw()
s.display()