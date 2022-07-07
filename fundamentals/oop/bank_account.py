class BankAccount:
    balance = 0
    intRate = 0

    def __init__(self, int_rate, balance): 
        self.intRate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Succesfully deposited", amount, "dollars")
        return self

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("Succesfully withdrew",amount, "dollars")
        elif self.balance >= 5:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance = 0
            print("Insufficient funds: Charging a $5 fee")
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.intRate/100) * self.balance
        return self
    print()

    @classmethod
    def printAllInfo(cls):
        print("The balance is:", cls.balance, "dollars")
        print("The interest is:", cls.intRate, "percent")

bankAccount1 = BankAccount(2, 100)
bankAccount2 = BankAccount(3, 400)

bankAccount1.deposit(100).deposit(150).deposit(50).withdraw(200).yield_interest().display_account_info()
print()
bankAccount2.deposit(200).deposit(100).withdraw(50).withdraw(150).withdraw(250).withdraw(100).yield_interest().display_account_info()
print()
bankAccount1.printAllInfo()


