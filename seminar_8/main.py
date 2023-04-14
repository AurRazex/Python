# id_client = 0
# data ={123: ('Sever','Alex','987','male'),
# 124: ('Chern','Evg','123','female')}
import export_import as ex
import model as m

phone_book = []

def menu(data: list):
    while True:
        print('выберите действие: ')
        print('0 - Выйти из справочника: ')
        print('1 - Создать новую запись: ')
        print('2 - Распечатать содержимое справочника: ')
        print('3 - Выбрать запись по первой части фамилии: ')
        print('4 - Изменить поле(я) выбранной записи: ')
        print('5 - Удалить записи из справочника: ')
        print('6 - Импортировать данные из файла: ')
        print('7 - Экспортировать данные в файл: ')

        get = input('Введите действие: ')
        if get == '0':
            print('Адьос!')
            break
        elif get == '1':
            data = m.create (data, m.get_data())
        elif get == '2':
            m.print_phone_book(data)
        elif get == '3':
            m.read(data)
        elif get == '4':
            m.update(data)
        elif get == '5':
            m.delete(data)
        elif get == '6':
            name_file = ex.get_file_name()
            batch_data = ex.get_batch_data(name_file)
            data = m.batch_create(data, batch_data)
        elif get == '7':
            name_file = ex.get_file_name()
            ex.record_data(name_file, data)
        else:
            print('Некорректный ввод данных, введите еще раз: ')



menu(phone_book)