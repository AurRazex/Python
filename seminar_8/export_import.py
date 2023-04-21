def get_file_name() -> str:
    return input('Введите имя файла: ')

def get_batch_data(name_file: str) -> list:
    lst = []
    with open('data01.txt', 'r', encoding = 'utf-8') as file:
        lst.extend(list(line.strip().split('#')) for line in file)
    return lst

def record_data(name_file, data):
    with open ('data01.txt', 'w', encoding = 'utf-8') as file:
        for el in data:
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')


