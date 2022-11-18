import ui, db, os.path


def user_selection():
    match ui.menu():
        case '1':
            db.add_contact()
            user_selection()
        case '2':
            db.del_contact()
            user_selection()
        case '3':
            ui.show_contacts()
            user_selection()
        case '4':
            filename = input('Введите имя импортируемого JSON-файла: ').strip()
            if os.path.isfile(filename):
                db.to_json(db.from_json(filename))
                print(f'{filename} успешно импортирован')
            else:
                print(f'{filename} не существует')
            user_selection()
        case '5':
            filename = input('Введите имя экспортируемого JSON-файла: ').strip()
            db.to_json(db.from_json(), filename)
            print(f'{filename} успешно экспортирован')
            user_selection()
        case '6':
            print('Спасибо за внимание)')
            exit()
        case _:
            print('Такого пункта нет')
            user_selection()
