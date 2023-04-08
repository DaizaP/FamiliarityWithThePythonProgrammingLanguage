# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# Решил сделать рандом
import random

i = 0
while i < 5:
    num = str(random.randint(100, 999))
    # print(num // 100, num // 10 % 10, num % 10) решил, что удобнее через строку
    res = int(num[0]) + int(num[1]) + int(num[2])
    print(num, '->', res, end=' ')
    print('({} + {} + {})'.format(num[0], num[1], num[2]))
    i += 1
