#Task-Bank Transaction Logger

class BankAccount:
    def __init__(self,name,__balance):
        self.name = name
        self.__balance = __balance


    def deposit(self,amount):
        self.amount = amount
        try:
            if amount < 0:
                raise ValueError("Amount cannot be negative")
            self.__balance+=amount
            log_transaction(self.name, "deposit", amount)

            
        except ValueError:
            print("ValueError has occurred")

    def withdraw(self,amount):
        self.amount = amount
        try:
            if amount > self.__balance:
                raise ValueError("Insufficient funds")
            self.__balance-=amount
            log_transaction(self.name, "withdraw", amount)
            
        except ValueError:
            print("ValueError has occurred")


    def __str__(self):
        return f"Account:{self.name} | Balance: {self.__balance}"
    


def log_transaction(name, action ,amount):
    with open("transactions.txt", "a")as f:
         f.write(f"{name} | {action} | {amount}\n ")

def load_transactions():
    try:
        with open("transactions.txt", "r") as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print("File not found exception has occurred")


acc = BankAccount("Smarika", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(5000)
acc.deposit(-1000)
load_transactions()
