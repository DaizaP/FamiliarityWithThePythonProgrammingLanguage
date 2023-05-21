# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def replace_file(data, find):
    with open(data, 'r', encoding='utf-8') as f:
        old_data = f.read()
    new_data = old_data.replace(*find, input('Введите ФИО и номер телефона через пробел:'))
    with open(data, 'w', encoding='utf-8') as f:
        f.write(new_data)
        f.close()
    print("Запись изменена")


def delete_file(data, find):
    with open(data, 'r', encoding='utf-8') as f:
        old_data = f.read()
    new_data = old_data.replace(str(*find)+'\n', '')
    with open(data, 'w', encoding='utf-8') as f:
        f.write(new_data)
        f.close()
    print("Запись удалена")


def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as data:
        dictionary = data.read().split('\n')
        data.close()
    return dictionary


def print_info(data):
    print(*readfile(data))


def export(data):
    text = readfile(data)
    res = input('Введите параметры поиска:')
    find = list(filter(lambda x: res in x, text))
    print(*find)
    my_choice = -1
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - внести изменения в запись\n'
              '2 - удалить запись\n'
              '0 - выход\n')
        my_choice = int(input())
        if my_choice == 0:
            return
        operations = {1: replace_file, 2: delete_file}
        data = 'tel.txt'
        operations[my_choice](data, find)


def import_in_file(data):
    res = open(data, 'a+', encoding='utf-8')
    res.write('\n' + input('Введите ФИО и номер телефона через пробел'))
    res.close()


def main():
    my_choice = -1
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - внести информацию в справочник(импорт)\n'
              '2 - поиск и вывод(экспорт)\n'
              '3 - вывести инфо на экран(весь список(экспорт))\n'
              '0 - выход из программы\n')
        my_choice = int(input())
        if my_choice == 0:
            exit()
        operations = {3: print_info, 2: export, 1: import_in_file}
        data = 'tel.txt'
        operations[my_choice](data)


if __name__ == '__main__':
    main()
