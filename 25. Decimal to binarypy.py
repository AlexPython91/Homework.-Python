# 25. Написать программу преобразования десятичного числа в двоичное
from random import randint

# number = 13
# print(bin(number))


def decimal_of_binarypy(number):
    result = []
    while number:
        result.append(number % 2)
        number = number // 2
    result.reverse()
    return result
print(decimal_of_binarypy(13))
