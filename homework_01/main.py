"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
   return list(map(lambda x: x ** 2, args))


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    value = 2
    while num % value != 0:
        value += 1
    return value == num


predicates = {
        "odd": lambda x: x % 2 != 0,
        "even": lambda x: x % 2 == 0,
        "prime": is_prime
    }


def filter_numbers(args, type):
    return list(filter(predicates[type], args))
