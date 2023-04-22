import modul as m


def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


sum_numbers(5)


def sum_numbers1(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


print(sum_numbers1(5))


def sum_numbers2(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa
    print('stop')  # не выполнится


print(sum_numbers2(5))


def sum_numbers3(n, y='Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


print(sum_numbers3(5, 'qwerty'))


def sum_str(*args):
    res = 0
    for i in args:
        res += i
    return res


print(sum_str(1, 2, 3))

print(m.max1(5, 9))

list_1 = []
for i in range(1, 10):
    list_1.append(m.fib(i))
print(list_1)

print(m.quick_sort([14, 9, 8, 5, 1, 9, 234, 12, 5, 8, 0, 8, 12345, 5, 3, 5, 7, 3, 32]))

list_2 = [1, 1, 2, 1, 312, 42, 545, 767, 6, 734, 432, 5354, 7756, 67, 8754, 3523, 45, 3457, 578]
m.merge_sort(list_2)
print(list_2)
