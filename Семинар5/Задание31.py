# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 8
# Output: 21
# Задание необходимо решать через рекурсию


def fib(n):
    if n < 2:
        temp[n] = n
        return n
    else:
        if temp[n] > 0:
            return temp[n]
        else:
            q = fib(n - 1) + fib(n - 2)
            temp[n] = q
            return q


temp = [0] * 100
for i in range(100):
    print(i, fib(i))
