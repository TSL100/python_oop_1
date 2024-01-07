class BalanceExeption(Exception):
    pass

class BankAccount:
    def __init__(self,initialAmount,accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' Created.\nBalance = $ {self.balance: .2f}")
    def getbalance(self):
        print(f"\nAccount '{self.name}' "
              f"Balance = $ {self.balance: .2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.getbalance()
    def VariableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
           raise BalanceExeption(
                f"\nSorry Account '{self.name}' only has a Balance of ${self.balance: .2f}"
            )
    def withdraw(self,amount):
        try:
            self.VariableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWith Draw Complete.")
            self.getbalance()
        except BalanceExeption as error:
            print(f"\nWith Draw Interrupted: {error}")
    def Transfer(self,amount,account):
        try:
            print(f"\n**********\n\n Beginning Transfer.. ")
            self.VariableTransaction(amount)
            print("\nTransfer Complete!\n\n*********")
        except BalanceExeption as error:
            print(f"\n Transfer Interrupted. {error}")
class InterestRewordsAcct(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print(f"\nDeposit complete.")
        self.getbalance()
class SavingAcct(InterestRewordsAcct):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount,accName)
        self.fee = 5
    def withdraw(self,amount):
        try:
            self.VariableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWith Draw Complete.")
            self.getbalance()
        except BalanceExeption as error:
            print(f"\nWith Draw Interrupted: {error}")

