class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        """Положить деньги на счет"""
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма должна быть положительной")
    
    def withdraw(self, amount):
        """Снять деньги со счета"""
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self.__balance:
            raise ValueError("Недостаточно средств")
        self.__balance -= amount
    
    def get_balance(self):
        """Получить текущий баланс"""
        return self.__balance

# Пример использования
account = BankAccount()

# Попытка снять деньги без депозита
try:
    account.withdraw(300)
except ValueError as e:
    print(f"Ошибка: {e}")

# Депозит
account.deposit(2000)
print(f"Баланс после депозита: {account.get_balance()}")

# Снятие средств
account.withdraw(100)
print(f"Баланс после снятия: {account.get_balance()}")

# Попытка снять больше, чем есть
try:
    account.withdraw(4000)
except ValueError as e:
    print(f"Ошибка: {e}")