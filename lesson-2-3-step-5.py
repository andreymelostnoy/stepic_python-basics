import itertools


def primes():
    a = 1
    while True:  # просто пример
        if a == 1:
            a += 1
        elif a == 2:
            a += 1
            yield a - 1
        elif a % 2 != 0:
            a += 1
            yield a - 1
        else:
            a += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
