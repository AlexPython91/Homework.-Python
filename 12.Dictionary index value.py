# 12. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

from random import randint

n = randint(1, 10)
print(n)

def get_dict(n):
    return {i: 3 * i + 1 for i in range(1, n + 1)}
print(get_dict(n))

