from tabulate import tabulate
import db


def start():
    print('''
    Добро пожаловать!
    Перед тобой упрощенный вариант телефонного справочника.
    Ты можешь создавать новые контакты, просматривать и удалять существующие.
    Также имеется возможность импорта и экспорта справочника в формате JSON.''')


def menu():
    print('''
    Выбери пункт меню:
        1. Добавить новый контакт
        2. Удалить контакт
        3. Показать все контакты
        4. Импортировать контакты из JSON-файла
        5. Экспортировать контакты в JSON-файл
        6. Выйти из справочника''')
    return input().strip()


def show_contacts():
    data = db.from_json()
    table = [i for i in data.values()]
    print(tabulate(table, headers='keys', tablefmt='rounded_outline'))
