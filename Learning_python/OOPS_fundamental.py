#OOPS fundamentals(inheritance,encapsulation)

class BankAccount:
    def __init__ (self,owner,balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,amount):
        if amount < 0:
            print("Balance cannot be negative")
        else:
            self__balance = amount

    def deposit(self,amount):
        self.__balance += amount
        print("The amount is",self.__balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            print("The amount is:",self.__balance)

    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"Account Owner: {self.owner} | Balance: {self.__balance}"
    

account =BankAccount("Smarika", 1000)
print(account)
print(account.balance)
account.balance = 500
account.balance = -100
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
print(account.get_balance())



#Inheritance in OOPS
class SavingsAccount(BankAccount):
    def __init__(self,owner,balance, interest_rate):
        super().__init__(owner,balance)
        self.__interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.__interest_rate
        self.deposit(interest)

acc =SavingsAccount("Smarika", 1000, 0.1)
acc.deposit(500)
acc.add_interest()
print(acc.get_balance())
print(acc)



