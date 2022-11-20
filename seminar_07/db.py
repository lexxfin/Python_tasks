from os.path import isfile
import json
import ui


def to_json(data: dict, filename='db.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def from_json(filename='db.json') -> dict:
    if not isfile(filename):
        with open(filename, 'w') as file:
            json.dump({}, file)
        return {}
    with open(filename, 'r') as file:
        return json.load(file)


def add_contact(data: dict):
    print('\nСоздание нового контакта:\n')
    id = str(int(list(data.keys())[-1]) + 1 if len(data) else 1)
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    bday = input('Введите день рождения: ')
    work = input('Введите место работы: ')
    phone = input('Введите номера телефонов через запятую: ').split(',')
    data[id] = {
        'id': id,
        'name': name,
        'surname': surname,
        'bday': bday,
        'work': work,
        'phone': phone
    }
    to_json(data)
    print('\nКонтакт успешно добавлен')
    ui.show_contacts(data)


def del_contact(data: dict):
    if len(data):
        ui.show_contacts(data)
        id = input('Введите id контакта, который нужно удалить: ').strip()
        if id in data.keys():
            del data[id]
            to_json(data)
            print('Контакт успешно удален')
            ui.show_contacts(data)
        else:
            print('Контакта с таким id нет в справочнике')
    else:
        print('В справочнике нет контактов')
