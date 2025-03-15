"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float) -> None:
        self.balance += income

    def reduce_balance(self, rate: float) -> None:
        self.balance -= rate

    def __str__(self) -> str:
        return f'Клиент: {self.owner_full_name}\nБаланс: {self.balance} руб.'

client_1 = BankAccount('Ivanov Ivan', 500.0)
client_2 = BankAccount('Petrov Petr', 250.0)


if __name__ == '__main__':
    print(client_1)
    print(client_2)
    client_1.increase_balance(233.3)
    client_2.reduce_balance(124.5)
    print(client_1)
    print(client_2)