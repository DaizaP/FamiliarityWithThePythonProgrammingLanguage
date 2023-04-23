import random


def fib(n):
    temp = [0, 1]
    print(0, temp[0])
    print(1, temp[1])
    for i in range(2, n + 1):
        temp.append(temp[i - 1] + temp[i - 2])
        print(i, temp[i])


def fib1(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def max_in_min(array):
    max1 = max(array)
    for j in range(len(array)):
        if array[j] == max1:
            array[j] = min(array)
    return array


def random_array(maxnum):
    return [random.randint(1, 5) for _ in range(int(maxnum))]


def task33(nums):
    list_1 = random_array(nums)
    print(len(list_1), '->', *list_1)
    list_1 = max_in_min(list_1)
    print('     ', *list_1)


def is_prime(nums):
    d = 2
    while d * d <= nums and nums % d != 0:
        d += 1
    return d * d > nums
