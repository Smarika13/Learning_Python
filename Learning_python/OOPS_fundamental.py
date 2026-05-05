#OOPS fundamentals

class BankAccount:
    def __init__ (self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("The amount is",self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("The amount is:",self.balance)

    def get_balance(self):
        return self.balance
    

account =BankAccount("Smarika", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
print(account.get_balance())

