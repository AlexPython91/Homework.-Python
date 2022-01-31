# 23. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

from random import randint
import math
my_list = [randint(2, 6) for i in range(5)]

def sum_number(my_list):
    new_list = []
    for i in range(len(my_list)):
        if i <= len(my_list) // 2: 
            new_list.append(my_list[i] * my_list[-i - 1])
    return new_list

print(my_list)
print(sum_number(my_list))

    