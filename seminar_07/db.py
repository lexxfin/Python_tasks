import json, os.path, ui


def to_json(data, filename='db.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def from_json(filename='db.json'):
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            json.dump(dict(), file)
    with open(filename, 'r') as file:
        return json.load(file)


def add_contact():
    data = from_json()
    id = int(list(data.keys())[-1]) + 1 if len(data) else 1
    print('\nСоздание нового контакта:\n')
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
    ui.show_contacts()


def del_contact():
    data = from_json()
    if len(data):
        ui.show_contacts()
        id = input('Введите id контакта, который нужно удалить: ').strip()
        if id in data.keys():
            del data[id]
            to_json(data)
            print('Контакт успешно удален')
            ui.show_contacts()
        else:
            print('Контакта с таким id нет в справочнике')
    else:
        print('В справочнике нет контактов.')
