list_1 = [1, 2, 3, 5, 8, 15, 23, 38]
# list_2 = [(i, i ** 2) for i in list_1 if i % 2 == 0]
list_2 = map(int, list_1)
list_2 = list(filter(lambda x: x % 2 == 0, list_2))
list_2 = list(map(lambda x: (x, x ** 2), list_2))
print(list_1)
print(list_2)
