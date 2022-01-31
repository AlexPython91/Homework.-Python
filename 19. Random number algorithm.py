# 19. Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

import datetime

def get_rand_number():
    return datetime.datetime.now().microsecond % 10

t = print(get_rand_number())
    
