from __future__ import division
import math


def get_factors(num):
    odd = num % 2 != 0
    factors = set()
    upper_bound = int(math.ceil(math.sqrt(num) + 1))
    for i in range(1, upper_bound, 2 if odd else 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors


def iterate_factors(start):
    num = start
    while True:
        yield (num, get_factors(sum(range(1, num + 1))))
        num += 1


def triange_iterator():
    num = 1
    while True:
        yield sum(range(1, num + 1))
        num += 1


def problem_12():
    triangles = triange_iterator()
    while True:
        triangle = next(triangles)
        factors = get_factors(triangle)
        if len(factors) > 500:
            return triangle


if __name__ == '__main__':
    print(problem_12())
