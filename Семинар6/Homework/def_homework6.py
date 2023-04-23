def is_prime(nums):
    d = 2
    while d * d <= nums and nums % d != 0:
        d += 1
    return d * d > nums


def progression(a1, d, n):
    res = ''
    if n <= 0:
        return res
    res += str(progression(a1, d, n - 1)) + ' ' + str(a1 + (n - 1) * d)
    return res


