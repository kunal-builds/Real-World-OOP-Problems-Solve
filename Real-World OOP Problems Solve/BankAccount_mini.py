#BankAccount Class (deposit + Withdrawal)

class BadBankAccount:
    def __init__(self, balance):
        self._balance = balance

class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property

    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Must have Postive Number")
        self._balance += amount

    def withdrawal(self, amount):
        if amount <= 0:
            raise ValueError("Must have Postive Number")
        if amount > self._balance:
            raise ValueError("Insuffician Funds")
        self._balance -= amount

account = BankAccount()
print(account._balance)
account.deposit(1.99)
print(account.balance)
account.withdrawal(1.99)
print(account.balance)

        