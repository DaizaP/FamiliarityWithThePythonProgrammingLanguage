# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7                         3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1            (каждое число вводится с новой строки)
import random
import my_def

arr1 = [random.randint(1, 10) for i in range(5)]
arr2 = [random.randint(1, 10) for i in range(5)]
arr3 = [i for i in arr1 if not(i in arr2)]
# arr3 = my_def.my_comparison(arr1, arr2)

print('Первый массив: ', *arr1)
print('Второй массив: ', *arr2)
print('Элементов, которых нет во втором массиве: ', *arr3)


