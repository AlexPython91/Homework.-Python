# 18. Реализовать алгоритм перемешивания списка. 

from random import randint
# Решение семинара:

my_list = [randint(1, 10) for i in range(10)]
print(my_list)

def shuffle_list(n):
    for i in range(len(n)-1):
        work_item = n[i]           
        index = randint(i + 1, len(n)-1)  
        n[i] = n[index]       
        n[index] = work_item
    return n
print(shuffle_list(my_list))



# Sample method:

# my_list = [1, 5, 12, 6, 7, 9]
# print(my_list)
# res = random.sample(my_list, len(my_list))
# print(str(res))



# Алгоритм Фишера – Йейтса:

# for i in range(len(my_list)-1, 0, -1):
#     j = randint(0, i + 1)
#     my_list[i], my_list[j] = my_list[j], my_list[i]
# print(my_list)

