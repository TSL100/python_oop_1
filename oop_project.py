from bank_accounts import *
Dave = BankAccount(1000,"Dave")
Sara = BankAccount(2000,"Sara")

Dave.getbalance()
Sara.getbalance()

Sara.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.Transfer(10000,Sara)

jim = InterestRewordsAcct(1000,"jim")

jim.getbalance()

jim.deposit(100)

jim.Transfer(100,Dave)

Blaze = SavingAcct(1000,"Blaze")

Blaze.getbalance()

Blaze.deposit(100)

Blaze.Transfer(10000,Sara)