def get_file_name() -> str:
    return input('Введите имя файла: ')

def get_batch_data(name_file: str) -> list:
    lst = []
    with open(input(), 'r', encoding = 'utf-8') as file:
        for line in file:
            lst.append(list(line.strip().split(';')))
    return lst

def record_data(name_file, data):
    with open (input(), 'w', encoding = 'utf-8') as file:
        for el in data:
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')


