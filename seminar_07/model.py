import ui
import db
from os.path import isfile


def user_selection():
    data = db.from_json()
    while True:
        match ui.menu():
            case '1':
                db.add_contact(data)
            case '2':
                db.del_contact(data)
            case '3':
                ui.show_contacts(data)
            case '4':
                filename = input('Введите имя импортируемого JSON-файла: ').strip()
                if isfile(filename):
                    data = db.from_json(filename)
                    db.to_json(data)
                    print(f'{filename} успешно импортирован')
                else:
                    print(f'{filename} не существует')
            case '5':
                if len(data):
                    filename = input('Введите имя экспортируемого JSON-файла: ').strip()
                    db.to_json(data, filename)
                    print(f'{filename} успешно экспортирован')
                else:
                    print('В справочнике нет контактов')
            case '6':
                print('Спасибо за внимание)')
                break
            case _:
                print('Такого пункта нет')
