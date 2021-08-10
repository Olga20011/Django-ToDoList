class Sacco:
    def __init__(self,name,accountNumber):
        self.name=name
        self.accountNumber=accountNumber
        self.balance=0
        self.loan=0

    def show_balance(self):
        return (f"Your account balance is {self.balance}")

    def deposit(self,amount):
        if amount<3000:
            print ("You can not deposit that amount")
        else:  
            self.balance+=amount  
            return (f"Your current balance is {self.balance}") 

    def withdraw(self,amount):
        self.balance-=amount
        return (f"You have withdrawn {amount} and your left with {self.balance}")

          

        
        