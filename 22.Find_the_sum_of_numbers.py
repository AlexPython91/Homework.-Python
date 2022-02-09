# 22. Найти сумму чисел списка стоящих на нечетной позиции

from random import randint

first_digit = 1
last_digit = 15
n = 10

def get_list(first_digit, last_digit, n):
    return [randint(first_digit, last_digit) for i in range(n)]

def find_sum_of_odd_numbers(new_list):
    return sum(new_list[::2])

new_list = get_list(first_digit, last_digit, n)
print(new_list)
print(find_sum_of_odd_numbers(new_list))