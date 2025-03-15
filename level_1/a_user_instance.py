"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str) -> None:
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone
    
    def __str__(self) -> str:
        return f'{self.name}, {self.username}, {self.age}, {self.phone}'
        

man = User("Ivan", "ivanthebest228", 18, "880005553535")
if __name__ == '__main__':
    print(man)
    

