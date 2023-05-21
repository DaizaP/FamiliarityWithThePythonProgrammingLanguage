# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

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
