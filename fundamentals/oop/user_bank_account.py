from bank_account import BankAccount
class User:

    def __init__(self, name, email, accountInt, accountBalance):
        self.name = name
        self.email = email
        self.account = BankAccount(accountInt, accountBalance)
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info