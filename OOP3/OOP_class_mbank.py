class MBankAccount:
    def __init__(self, account_number_pm: int, balance_pm: int = 0.0):
        self._account_number = account_number_pm
        self._balance = balance_pm

    def deposit(self, amount_pm):
        if amount_pm > 0:
            self._balance += amount_pm
            print(f"Deposited {amount_pm}. New balance is {self._balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                print(f"Withdrew {amount}. New balance is {self._balance}.")

            else:
                print("Недостаточно Средств.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self._balance

# Примеры использования класса

# Создаем объект MBankAccount
account = MBankAccount("123456789", 1000)

# Делаем депозит
account.deposit(500)

# Пытаемся снять средства
account.withdraw(200)

# Пытаемся снять средства, превышающие баланс
account.withdraw(1500)

# Отображаем текущий баланс
print(f"Current balance: {account.get_balance()}")
