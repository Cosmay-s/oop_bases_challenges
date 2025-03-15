"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float) -> None:
        self.balance += income

    def __str__(self) -> str:
        return f'Клиент: {self.owner_full_name}\nБаланс: {self.balance} руб.'

client_1 = BankAccount('Ivanov Ivan', 500.0)
client_2 = BankAccount('Petrov Petr', 250.0)


if __name__ == '__main__':
    print(client_1)
    print(client_2)
    client_1.increase_balance(233.3)
    print(client_1)
    print(client_2)
