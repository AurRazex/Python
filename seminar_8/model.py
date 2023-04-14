def create(data: list, el: list) -> list: # добавляет запись в существующую книгу
    data.append(el)
    return data

def batch_create(data: list, batch_data) -> list:
    for el in batch_data:
        data = create(data, el)
    return data

def print_phone_book(data: list) -> None:  # Распечетывает добавленые записи
        print(f'контакты:  {data}')

def get_data() -> list:
    surname = input('введите фамилию: ')
    name = input('введите имя: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    return (surname, name, phone, discription) # type: ignore

def get_file_name() -> str:
    return input('Введите имя файла: ')

def read(data: list) -> list:  # Поиск человека # type: ignore
    part_surname = input('Введите первые буквы фамилии: ')
    for el in data:
        if part_surname.casefold() in (el[0]).casefold():
            return el

def update(data: list) -> list: # Изменение данных в справочнике
    change_contact = read(data)

    while True:
        print(f'вы выбрали: {change_contact}')
        print('Выберите действие: ')
        print('0 - Выйти в главное меню: ')
        print('1 - Изменить Фамилию: ')
        print('2 - Изменить Имя: ')
        print('3 - Изменить телефон: ')
        print('4 - Изменить Описание: ')

        for el in data:
            if el == change_contact:
                get_action = input('Введите действие: ')
                if get_action =='0':
                    print('Успешно!')
                    break
                elif get_action =='1':
                    change_contact[0] = input('Введите Фмаилию: ')
                elif get_action =='2':
                    change_contact[1] = input('Введите Имя: ')
                elif get_action =='3':
                    change_contact[2] = input('Введите телефон: ')
                elif get_action =='4':
                    change_contact[3] = input('Введите описание: ')
                else:
                    print('некорректный ввод данных!')
                el = change_contact
        return data

def delete(data: list) -> list: # Удаление записи из списка
    del_contact = read(data)
    print(f'Вы удалили: {del_contact}')
    for el in data:
        if el == del_contact:
            data.remove(el)
            break
    return data



