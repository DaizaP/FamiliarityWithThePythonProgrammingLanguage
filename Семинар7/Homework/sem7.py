def ritm(vinny):
    vinny = vinny.lower().split()
    word = 'уеёыаоэяию'
    res = list(map(lambda x: sum(1 for i in x if i in word), vinny))
    if all(res):
        print('Парам пам-пам')
    else:
        print('Пам парам')


def print_operation_table(operation, num_rows=6, num_columns=6):
    res = list([operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1))
    for i in res:
        print(*[f"{x:>3}" for x in i])
