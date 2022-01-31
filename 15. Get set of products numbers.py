# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

from unittest import result


def get_set_of_numbers(n):
    x = 1
    result = []
    for i in range(1, n + 1):
        x = x * i
        result.append(x)
    return result
print(get_set_of_numbers(5))
