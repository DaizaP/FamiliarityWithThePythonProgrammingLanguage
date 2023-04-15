# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
# 1 2 3 4 5
# 6
# -> 5
import random

n = int(input('Введите кол-во элементов в массиве: '))
a = [random.randint(-100, 100) for i in range(n)]
x = int(random.randint(-100, 100))
print(n)
result = -1
difference = abs(max(a)) if abs(max(a)) > abs(min(a)) else abs(min(a))    # ищем максимальную разницу
print(difference)
for i in range(len(a)):
    print(a[i], end=' ')
    if abs(a[i] - x) < difference:
        result = a[i]
        difference = abs(a[i] - x)
print()
print(x)
print('->', result, difference)
