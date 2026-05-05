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
    
    def __str__(self):
        return f"Account Owner: {self.owner} | Balance: {self.balance}"
    

account =BankAccount("Smarika", 1000)
print(account)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
print(account.get_balance())



#Inheritance in OOPS
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance, interest_rate):
        super().__init__(owner,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

acc =SavingsAccount("Smarika", 1000, 0.1)
acc.deposit(500)
acc.add_interest()
print(acc.get_balance())
print(acc)


