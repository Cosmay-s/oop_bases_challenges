"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: int, weihgt: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.weight = weihgt

    def __str__(self) -> str:
        return f'Информация о продукте:\nНазвание: {self.name}\nОписание: {self.description}\nЦена: {self.price} руб.\nВес: {self.weight} гр.'

banana = Product("Бананы", "Желтые, вкусные и питательные.", 100, 1000)


if __name__ == '__main__':
    print(banana)
