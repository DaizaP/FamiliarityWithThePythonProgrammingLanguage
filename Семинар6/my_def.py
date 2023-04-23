from sympy import divisors


def my_comparison(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        if arr1[i] not in arr2:
            arr3.append(arr1[i])
    return arr3


def my_count(arr1):
    cnt = 0
    for i in range(1, len(arr1) - 1):
        if arr1[i - 1] < arr1[i] and arr1[i + 1] < arr1[i]:
            cnt += 1
    return cnt


def find_neighbors_of_number(number, array1):
    count_of_neighbors = 0
    for i in range(1, len(array1) - 1):
        if (array1[i - 1] < number) and (array1[i + 1] < number):
            count_of_neighbors = count_of_neighbors + 1
    return count_of_neighbors


def is_prime(nums):
    d = 2
    while d * d <= nums and nums % d != 0:
        d += 1
    return d * d > nums


def new_is_prime(index):
    arris_prime = [True] * (index + 1)
    arris_prime[0] = False
    arris_prime[1] = False
    d = 2
    while d * d <= index:
        if arris_prime[d]:
            for i in range(d * d, index + 1, d):
                arris_prime[i] = False
        d += 1


def prime(nums=10 ** 5):
    n = [n for n in range(1, nums) if
         sum(divisors(n)) - 2 * n and not sum(divisors(sum(divisors(n)) - n)) - sum(divisors(n))]
    return n
