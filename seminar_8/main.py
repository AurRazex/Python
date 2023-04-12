phone_book = []

def menu(data: dict, id_client: int):
    while True:
        print('выберите действие: ') 
        print('0 - Выйти из справочника')
        print('1 - Создать новую запись')
        print('2 - Распечатать содержимое справочника')
        print('3 - Выбрать запись по первой части фамилии')
        print('4 - Изменить поле(я) выбранной записи')
        print('5 - Удалить записи из справочника')
        print('6 - Импортировать данные из файла')
        print('7 - Экспортировать данные в файл')

        get = input('Введите действие: ')
        if get == '0':
            print('Адьос!')
            break
        elif get == '1':
            data = create (data, id_client, get_data())
        elif get == '2':
            print_phone_book(data)
        elif get == '3':
            read(data)
        elif get == '4':
            update(data)
        elif get == '5':
            delete(data)
        elif get == '6':
            name_file = get_file_name()
            batch_data = get_batch_data(name_file)
            data = batch_create(data, batch_data, id_client)
        elif get == '7':
            name_file = get_file_name()
            record_dara(name_file, data)
        else:
            print('Некорректный ввод данных, введите еще раз: ')