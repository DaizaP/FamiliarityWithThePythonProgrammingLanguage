# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что
# Петя и Сережа сделали одинаковое количество журавликов, а
# Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
import random
import time

# 6 частей. 1 Петя. 1 Сергей. 4 Катя(в два раза больше чем Сергей и Петя)
s = random.randint(10, 100)
# Ищем число, которое будет нацело делиться на шесть частей(иначе дети будут делать не целое кол-во журавликов)
while s % 6 != 0:
    print('Сгенерированное число', s, 'не подходит, выбираем другое')
    time.sleep(0.5) # Для красоты, другого смысла нет
    s = random.randint(10, 100)
print('Число', s, 'подходит')
time.sleep(0.5) # Тоже для красоты
Petya = int(s / 6)
Sergey = int(Petya)
Kate = int(Petya * 4)
print(s, '->', '({} + {} + {})'.format(Petya, Kate, Sergey))
time.sleep(0.5)
